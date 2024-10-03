import json
import torch
import typing
import re
import string

# Local Files
from ..utils.file_utils import safe_open_w
from ..utils.label_prompt_funcs import textlabel_2_binarylabel, label_2_SemEval2024, create_qdid_prompt
from ..evaluation.SemEval2024_sourceEval import calc_scores

# Util libs
from datetime import datetime
from tqdm import tqdm
from itertools import zip_longest

#def tokenize_generate_five_decode(model : object, tokenizer : object, text : str, max_new_tokens : int = 50, top_k : int = 5, top_p : float = 0, do_sample : bool = True, temperature : float = 1.0) -> str:   
#    tokenized = tokenizer(text, return_tensors="pt")
#    tokenized["input_ids"] = tokenized.input_ids.to(device="cuda")
#    tokenized["attention_mask"] = tokenized.attention_mask.to(device="cuda")
#
#    # We could use do_sample=False and disable top_k and top_p to get a deterministic output
#    outputs = model.generate(**tokenized, max_new_tokens=max_new_tokens, top_k = top_k, top_p = top_p, do_sample=do_sample, temperature = temperature, pad_token_id=tokenizer.eos_token_id, num_return_sequences= 10)
#
#    return [re.sub("(</s>)*", "", tokenizer.decode(out[tokenized["input_ids"].shape[1]:]).strip()) for out in outputs]

def batch_tokenize_decode(model : object, tokenizer : object, text_list : list[str], max_new_tokens : int = 50, top_k : int = 5, top_p : float = 0.10, do_sample : bool = True, temperature : float = 0.1):
    tokenized = tokenizer(text_list, return_tensors="pt", padding=True).to(device="cuda")

    outputs = model.generate(**tokenized, max_new_tokens=max_new_tokens, top_k = top_k, top_p = top_p, do_sample=do_sample, temperature = temperature, pad_token_id=tokenizer.eos_token_id)
    
    #TO:DO This is not working properly. It's cutting the output based on the longest input
    token_outputs = [outputs[i][tokenized["input_ids"][i].shape[0]:] for i in range(len(outputs))]
    print([decoded.strip() for decoded in tokenizer.batch_decode(token_outputs, skip_special_tokens=True)])

    return [decoded.strip() for decoded in tokenizer.batch_decode(token_outputs, skip_special_tokens=True)]


def tokenize_generate_decode(model : object, tokenizer : object, text : str, max_new_tokens : int = 50, top_k : int = 50, top_p : float = 0.95, do_sample : bool = True, temperature : float = 1.0) -> str:   
    tokenized = tokenizer(text, return_tensors="pt")
    tokenized["input_ids"] = tokenized.input_ids.to(device="cuda")
    tokenized["attention_mask"] = tokenized.attention_mask.to(device="cuda")

    outputs = None
    if do_sample:
        # We could use do_sample=False and disable top_k and top_p to get a deterministic output
        outputs = model.generate(**tokenized, max_new_tokens=max_new_tokens, top_k = top_k, top_p = top_p, do_sample=do_sample, temperature = temperature, pad_token_id=tokenizer.eos_token_id)
    else:
        outputs = model.generate(**tokenized, max_new_tokens=max_new_tokens, do_sample=False, pad_token_id=tokenizer.eos_token_id)
    
    return tokenizer.decode(outputs[0][tokenized["input_ids"].shape[1]:]).strip()

def query_inference(model : object, tokenizer : object, queries : dict, args : object) -> dict:
    res_labels = {}
    answers = {}

    with torch.inference_mode():
        query_keys = list(queries.keys())
        batched_queries = []
        for i in range(0, len(query_keys), args.batch_size):
            batched_queries.append(query_keys[i:i+args.batch_size])

        batched_answers = []
        for batch in tqdm(batched_queries):
            decoded_output = batch_tokenize_decode(model, tokenizer, [queries[q_id]["text"] for q_id in batch], args.max_new_tokens, args.top_k, args.top_p, args.sample, args.temperature)

            batched_answers += decoded_output
        
        for i in range(len(query_keys)):
            answer = re.sub("(<\/s>)+", " ", batched_answers[i])

            answers[query_keys[i]] = answer
            answer = answer.translate(str.maketrans('', '', string.punctuation))

            res_labels[query_keys[i]] = None
            if args.task_type == 'base_inference':
                res_labels[query_keys[i]] = textlabel_2_binarylabel(answer.split(" "))

            elif args.task_type == 'CoT_Inference':
                res_labels[query_keys[i]] = textlabel_2_binarylabel(answer.split(" ")[::-1])

    return res_labels, answers


def output_prompt_labels(model : object, tokenizer : object, queries : dict, prompt : str, args : object, used_set : str):

    queries_dict, pred_labels, answers = None, None, None

    # Replace prompt with query info
    if args.task_type == 'base_inference' or args.task_type == "CoT_inference":
        queries_dict = create_qdid_prompt(queries, prompt)
        pred_labels, answers = query_inference(model, tokenizer, queries_dict, args)

    elif args.task_type == "ICL_inference":
        queries_dict = create_qdid_prompt(queries, prompt)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

    exp_name = args.exp_name if "exp_name" in args else ""

    with safe_open_w(f'{args.output_dir}{exp_name if exp_name != "" else ""}_FULL-ANSWERS_{timestamp}_{used_set}-set.json') as output_file:
        output_file.write(json.dumps(answers, ensure_ascii=False, indent=4))

    # Output results
    with safe_open_w(f'{args.output_dir}{exp_name if exp_name != "" else ""}_{timestamp}_{used_set}-set.json') as output_file:
        preds = label_2_SemEval2024(pred_labels)
        output_file.write(json.dumps(preds, ensure_ascii=False, indent=4))

        calc_scores(preds, f'{exp_name if exp_name != "" else ""}_{timestamp}_{used_set}-set.json', args.output_dir, args)

#def example_inference(model : object, tokenizer : object, queries : dict) -> dict:
#    res_labels = {}
#    answers = {}
#
#    with torch.inference_mode():
#        for q_id in tqdm(queries):
#            decoded_output = tokenize_generate_decode(model, tokenizer, queries[q_id]["text"], 50, 50, 0.95, True)
#
#            decoded_output_sub = re.sub("(<\/s>)+", " ", decoded_output)
#
#            answers[q_id] = decoded_output_sub
#            res_labels[q_id] = textlabel_2_binarylabel(decoded_output_sub.split(" "))
#    return res_labels, answers