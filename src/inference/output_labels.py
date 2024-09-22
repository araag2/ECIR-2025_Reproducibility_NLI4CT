import json
import torch
import typing
import re

# Local Files
from ..utils.file_utils import safe_open_w
from ..utils.label_prompt_funcs import textlabel_2_binarylabel, label_2_SemEval2024, create_qdid_prompt
from ..evaluation.SemEval2024_sourceEval import calc_scores

# Util libs
from datetime import datetime
from tqdm import tqdm

def tokenize_generate_decode_no_sample(model : object, tokenizer : object, text : str, max_new_tokens : int = 5) -> str:   
    tokenized = tokenizer(text, return_tensors="pt")
    tokenized["input_ids"] = tokenized.input_ids.to(device="cuda")
    tokenized["attention_mask"] = tokenized.attention_mask.to(device="cuda")

    # We could use do_sample=False and disable top_k and top_p to get a deterministic output
    outputs = model.generate(**tokenized, max_new_tokens=max_new_tokens, do_sample=False, pad_token_id=tokenizer.eos_token_id)
    
    return tokenizer.decode(outputs[0][tokenized["input_ids"].shape[1]:]).strip()

def tokenize_generate_decode(model : object, tokenizer : object, text : str, max_new_tokens : int = 50, top_k : int = 50, top_p : float = 0.95, do_sample : bool = True, temperature : float = 1.0) -> str:   
    tokenized = tokenizer(text, return_tensors="pt")
    tokenized["input_ids"] = tokenized.input_ids.to(device="cuda")
    tokenized["attention_mask"] = tokenized.attention_mask.to(device="cuda")

    # We could use do_sample=False and disable top_k and top_p to get a deterministic output
    outputs = model.generate(**tokenized, max_new_tokens=max_new_tokens, top_k = top_k, top_p = top_p, do_sample=do_sample, temperature = temperature, pad_token_id=tokenizer.eos_token_id)
    
    return tokenizer.decode(outputs[0][tokenized["input_ids"].shape[1]:]).strip()

def tokenize_generate_five_decode(model : object, tokenizer : object, text : str, max_new_tokens : int = 50, top_k : int = 5, top_p : float = 0, do_sample : bool = True, temperature : float = 1.0) -> str:   
    tokenized = tokenizer(text, return_tensors="pt")
    tokenized["input_ids"] = tokenized.input_ids.to(device="cuda")
    tokenized["attention_mask"] = tokenized.attention_mask.to(device="cuda")

    # We could use do_sample=False and disable top_k and top_p to get a deterministic output
    outputs = model.generate(**tokenized, max_new_tokens=max_new_tokens, top_k = top_k, top_p = top_p, do_sample=do_sample, temperature = temperature, pad_token_id=tokenizer.eos_token_id, num_return_sequences= 10)

    return [re.sub("(</s>)*", "", tokenizer.decode(out[tokenized["input_ids"].shape[1]:]).strip()) for out in outputs]

def query_inference(model : object, tokenizer : object, queries : dict, sample : bool = True) -> dict:
    res_labels = {}

    with torch.inference_mode():
        for q_id in tqdm(queries):
            decoded_output = ""

            if sample:
                decoded_output = tokenize_generate_decode(model, tokenizer, queries[q_id]["text"], 5, 15, 0.7, True)
            else:
                decoded_output = tokenize_generate_decode_no_sample(model, tokenizer, queries[q_id]["text"], 5)

            decoded_output_sub = re.sub("(<\/s>)+", " ", decoded_output)

            res_labels[q_id] = textlabel_2_binarylabel(decoded_output_sub.split(" "))
    return res_labels


def output_prompt_labels(model : object, tokenizer : object, queries : dict, prompt : str, args : object, used_set : str):
    # Replace prompt with query info
    queries_dict = create_qdid_prompt(queries, prompt)

    # 0-shot inference from queries
    pred_labels = query_inference(model, tokenizer, queries_dict, args.sample)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

    exp_name = args.exp_name if "exp_name" in args else ""

    # Output results
    with safe_open_w(f'{args.output_dir}{exp_name if exp_name != "" else ""}_{timestamp}_{used_set}-set.json') as output_file:
        preds = label_2_SemEval2024(pred_labels)
        output_file.write(json.dumps(preds, ensure_ascii=False, indent=4))

        calc_scores(preds, f'{exp_name if exp_name != "" else ""}{timestamp}_{used_set}-set.json', args.output_dir)