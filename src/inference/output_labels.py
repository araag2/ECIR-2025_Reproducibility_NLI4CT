import json
import torch
import typing
import re
import string
import time

# Local Files
from ..utils.file_utils import safe_open_w
from ..utils.label_prompt_funcs import textlabel_2_binarylabel, textlabelgroup_2_binarylabel, label_2_SemEval2024, create_qdid_prompt, textlabel_2_binarylabel_CoT
from ..evaluation.SemEval2024_sourceEval import calc_scores

# Util libs
from datetime import datetime
from tqdm import tqdm

def tokenize_generate_decode(model : object, tokenizer : object, text_list : list[str], max_new_tokens : int = 50, top_k : int = 5, top_p : float = 0.10, do_sample : bool = True, temperature : float = 0.1, num_return_sequences : int = 1) -> list[str]:
    tokenized = tokenizer(text_list, return_tensors="pt", padding=True).to(device="cuda")

    outputs = model.generate(**tokenized, max_new_tokens=max_new_tokens, top_k = top_k, top_p = top_p, do_sample=do_sample, temperature = temperature, num_return_sequences=num_return_sequences, pad_token_id=tokenizer.eos_token_id)

    new_tokens = []
    if num_return_sequences == 1:
        for i in range(len(text_list)):
            non_special_ids = (tokenized["attention_mask"][i]==1).nonzero(as_tuple=True)[0]
            first_non_special = non_special_ids[0]
            new_tokens.append(outputs[i][len(non_special_ids) + first_non_special:])
    
    else:
        for i in range(len(text_list)):
            for j in range(num_return_sequences):
                non_special_ids = (tokenized["attention_mask"][i]==1).nonzero(as_tuple=True)[0]
                first_non_special = non_special_ids[0]
                new_tokens.append(outputs[i*num_return_sequences + j][len(non_special_ids) + first_non_special:])

    return [decoded for decoded in tokenizer.batch_decode(new_tokens, skip_special_tokens=True)]

def clean_text(text : str) -> str:
    text = re.sub("\n", " ", re.sub("(<\/s>)+", " ", text))
    return text.translate(str.maketrans('', '', string.punctuation))

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
            decoded_output = tokenize_generate_decode(model, tokenizer, [queries[q_id]["text"] for q_id in batch], args.max_new_tokens, args.top_k, args.top_p, args.sample, args.temperature, args.num_return_sequences)

            batched_answers += decoded_output
        
        for i in range(len(query_keys)):
            if args.task_type in ['base_inference', 'icl_inference_1-shot', 'icl_inference_2-shot']:
                answers[query_keys[i]] = clean_text(batched_answers[i])
                res_labels[query_keys[i]] = textlabel_2_binarylabel(answers[query_keys[i]].split(" "))

            elif args.task_type in ['CoT_inference', 'icl_inference_CoT-ver_1-shot', 'icl_inference_CoT-ver_2-shot']:
                answers[query_keys[i]] = clean_text(batched_answers[i])
                reverse_answer = answers[query_keys[i]].split(" ")[::-1]

                res_labels[query_keys[i]] = textlabel_2_binarylabel_CoT(reverse_answer)

            elif args.task_type == 'self-consistency_inference':
                answers[query_keys[i]] = [clean_text(answer) for answer in batched_answers[i*args.num_return_sequences:(i+1)*args.num_return_sequences]]
                res_labels[query_keys[i]] = textlabelgroup_2_binarylabel([answer.split(" ") for answer in answers[query_keys[i]]])

            elif args.task_type == 'self-consistency_CoT_inference':
                answers[query_keys[i]] = [clean_text(answer) for answer in batched_answers[i*args.num_return_sequences:(i+1)*args.num_return_sequences]]

                res_labels[query_keys[i]] = textlabel_2_binarylabel_CoT([answer.split(" ")[::-1] for answer in answers[query_keys[i]]])

    return res_labels, answers


def output_prompt_labels(model : object, tokenizer : object, queries : dict, prompt : str, args : object, used_set : str):

    queries_dict, pred_labels, answers = None, None, None

    # Replace prompt with query info
    queries_dict = create_qdid_prompt(queries, prompt, args)
    pred_labels, answers = query_inference(model, tokenizer, queries_dict, args)

    args.timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

    exp_name = args.exp_name if "exp_name" in args else ""

    # Output results
    with safe_open_w(f'{args.output_dir}FULL-ANSWERS_{exp_name if exp_name != "" else ""}_Seed-{args.random_seed}.json') as output_file:
        preds = label_2_SemEval2024(pred_labels)
        output_formatting = {key : {'text_answer' : answers[key], 'label' : preds[key]["Prediction"]} for key in answers}
        output_file.write(json.dumps(output_formatting, ensure_ascii=False, indent=4))

        calc_scores(preds, f'{exp_name if exp_name != "" else ""}_Seed-{args.random_seed}.json', args.output_dir, args)

def gemini_inference(model : object, queries : dict, gen_config : dict, safety_config : dict, args : object) -> dict:
    res_labels = {}
    answers = {}

    query_keys = list(queries.keys())
    
    batched_queries = []
    for i in range(0, len(query_keys), args.batch_size):
        batched_queries.append(query_keys[i:i+args.batch_size])

    batched_answers = []
    for batch in tqdm(batched_queries):
        for q_id in batch:
            try:
                response = model.generate_content(queries[q_id]["text"],
                                              generation_config=gen_config,
                                              safety_settings=safety_config
                )
                batched_answers.append(response.text)

            except Exception as e:
                print(e)
                batched_answers.append("")

            #time.sleep(0.05)
    
    for i in range(len(query_keys)):
        answers[query_keys[i]] = clean_text(batched_answers[i])
        res_labels[query_keys[i]] = textlabel_2_binarylabel(answers[query_keys[i]].split(" "))

    return res_labels, answers


def output_prompt_labels_gemini(model : object, queries : dict, prompt : str, gen_config : dict, safety_config : dict, args : object):
    queries_dict, pred_labels, answers = None, None, None

    # Replace prompt with query info
    queries_dict = create_qdid_prompt(queries, prompt, args)
    pred_labels, answers = gemini_inference(model, queries_dict, gen_config, safety_config, args)

    args.timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M")

    exp_name = args.exp_name if "exp_name" in args else ""

    # Output results
    with safe_open_w(f'{args.output_dir}FULL-ANSWERS_{exp_name if exp_name != "" else ""}_Seed-{args.random_seed}.json') as output_file:
        preds = label_2_SemEval2024(pred_labels)
        output_formatting = {key : {'text_answer' : answers[key], 'label' : preds[key]["Prediction"]} for key in answers}
        output_file.write(json.dumps(output_formatting, ensure_ascii=False, indent=4))

        calc_scores(preds, f'{exp_name if exp_name != "" else ""}_Seed-{args.random_seed}.json', args.output_dir, args)