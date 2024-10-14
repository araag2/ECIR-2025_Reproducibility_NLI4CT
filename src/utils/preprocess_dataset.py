import json
import argparse
import typing

from .file_utils import safe_open_w
from .label_prompt_funcs import create_qid_prompt_label_dict


def preprocess_dataset(args : argparse, prompt : str , used_set : str):
    # Load JSON
    set_examples = create_qid_prompt_label_dict(json.load(open(f'{args.queries}queries2024_{used_set}.json')), json.load(open(f'{args.qrels}qrels2024_{used_set}.json')), prompt, args.task_type if "task_type" in args else "base")
    
    set_dict = {"id" : [], "text" : []}
    for q_id in set_examples:
        example = set_examples[q_id]
        set_dict["id"].append(q_id)
        label = "Yes</s>" if example["gold_label"] == 1 else "No</s>"
        set_dict["text"].append(f'{example["text"]}{label}')
    return set_dict

def preprocess_conjoint_dataset(args : argparse, used_set : str):
    base_queries = json.load(open(f'{args.queries}queries2024_{used_set}.json'))
    base_qrels = json.load(open(f'{args.qrels}qrels2024_{used_set}.json'))

    task_type_prompts = {
        "base" : {"prompt" : json.load(open(args.prompt_file))["base_prompt"], "queries" : {}, "qrels" : {}},

        "self_consistency" : {"prompt" : json.load(open(args.prompt_file))["self-consistency_prompt"], "queries" : {}, "qrels" : {}},

        "section_info" : {"prompt" : json.load(open(args.prompt_file))["section_info_prompt"], "queries" : {}, "qrels" : {}}
    }

    for q_id in base_queries:
        used_set_id = q_id.split("_")
        if used_set_id[-1] in task_type_prompts:
            task_type_prompts[used_set_id[-1]]["queries"][q_id] = base_queries[q_id]
            task_type_prompts[used_set_id[-1]]["qrels"][q_id] = base_qrels[q_id]

    set_dict = {"id" : [], "text" : []}

    for task_type in task_type_prompts:
        res = create_qid_prompt_label_dict(task_type_prompts[task_type]["queries"], task_type_prompts[task_type]["qrels"], task_type_prompts[task_type]["prompt"], task_type)

        for q_id in res:
            example = base_queries[q_id]
            set_dict["id"].append(q_id)
            label = "YES" if base_qrels[q_id] == 1 else "NO"
            set_dict["text"].append(f'{example} Answer: {label}')

    return set_dict

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--prompt_file", default="src/prompts/Baseline_Prompts.json", type=str)
    parser.add_argument("--prompt_name", default="Mistral7B_short-prompt", type=str)

    parser.add_argument("--used_set", default="train", type=str)
    parser.add_argument("--queries", default="data/SemEval-2024/queries/", type=str)
    parser.add_argument("--qrels", default="data/SemEval-2024/qrels/", type=str)

    parser.add_argument('--output_dir', type=str, default="data/SemEval-2024/training_preprocessed_data/", help='path to save preprocessed data')

    args = parser.parse_args()

    preprocessed_dataset = preprocess_dataset(args, json.load(open(args.prompt_file))[args.prompt_name], args.used_set)

    with safe_open_w(f'{args.output_dir}Preprocessed-Data_{args.used_set}-set.json') as output_file:
        output_file.write(json.dumps(preprocessed_dataset, ensure_ascii=False, indent=4))

if __name__ == '__main__':
    main()