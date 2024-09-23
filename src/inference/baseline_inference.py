import argparse
import json
import torch
import datetime

# Model Libs
from transformers import AutoTokenizer, AutoModelForCausalLM
from peft import PeftModel

from .output_labels import output_prompt_labels

def main():
    parser = argparse.ArgumentParser()

    # Model and checkpoint paths, including a merging flag
    parser.add_argument('--model', type=str, help='name of the model used to generate and combine prompts', default='')
    parser.add_argument('--exp_name', type=str, help='name of the experiment', default='')

    # Path to queries, qrels and prompt files
    parser.add_argument('--used_set', type=str, help='choose which data to use', default='') # train | dev | test
    args = parser.parse_known_args()

    parser.add_argument('--queries', type=str, help='path to queries file', default=f'')
    parser.add_argument('--qrels', type=str, help='path to qrels file', default=f'')
    
    parser.add_argument('--prompt_file', type=str, help='path to prompts file', default='')
    parser.add_argument('--prompt_name', type=str, help='name of the prompt to use', default='')

    # sampling ON or OFF
    parser.add_argument('--sample', dest='sample', action='store_true', help='boolean flag to set if model is merging')
    parser.add_argument('--no_sample', dest='sample', action='store_false', help='boolean flag to set if model is merging')
    parser.set_defaults(sample=True)
    
    # Output directory
    parser.add_argument('--output_dir', type=str, help='path to output_dir', default="outputs/")

    args = parser.parse_args()

    model = AutoModelForCausalLM.from_pretrained(
        args.model, low_cpu_mem_usage=True,
        return_dict=True, torch_dtype=torch.bfloat16,
        device_map= {"": 0}, attn_implementation="flash_attention_2"
    )

    tokenizer = AutoTokenizer.from_pretrained(args.model)
    tokenizer.pad_token_id = tokenizer.eos_token_id

    # Load dataset, queries, qrels and prompts
    queries = json.load(open(args.queries))
    qrels = json.load(open(args.qrels))
    prompt = json.load(open(args.prompt_file))[args.prompt_name]

    output_prompt_labels(model, tokenizer, queries, prompt, args, args.used_set)

if __name__ == '__main__':
    main()