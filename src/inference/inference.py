import argparse
import json
import torch
import datetime
import random

# Model Libs
from transformers import AutoTokenizer, AutoModelForCausalLM, set_seed
from peft import PeftModel

from .output_labels import output_prompt_labels

def set_random_seed(random_seed = 0):
    random.seed(random_seed)
    set_seed(random_seed)
    torch.manual_seed(random_seed)
    if torch.cuda.is_available():
        torch.cuda.manual_seed(random_seed)
        torch.cuda.manual_seed_all(random_seed)

def main():
    parser = argparse.ArgumentParser()

    # Model and checkpoint paths
    parser.add_argument('--model', type=str, help='name of the model used to generate and combine prompts', default='')
    parser.add_argument('--exp_name', type=str, help='name of the experiment', default='')

    # Merge Params
    parser.add_argument('--checkpoint', type=str, help='path to model checkpoint, used if merging', default="")

    # Path to queries, qrels and prompt files
    parser.add_argument('--used_set', type=str, help='choose which data to use', default='') # train | dev | test
    args = parser.parse_known_args()

    parser.add_argument('--queries', type=str, help='path to queries file', default=f'')
    parser.add_argument('--qrels', type=str, help='path to qrels file', default=f'')
    
    parser.add_argument('--prompt_file', type=str, help='path to prompts file', default='')
    parser.add_argument('--prompt_name', type=str, help='name of the prompt to use', default='')

    # Generation Params
    parser.add_argument('--batch_size', type=int, help='batch_size of generated examples', default=8)

    parser.add_argument('--sample', dest='sample', action='store_true', help='boolean flag to set if model is merging')
    parser.add_argument('--no_sample', dest='sample', action='store_false', help='boolean flag to set if model is merging')
    parser.set_defaults(sample=True)

    parser.add_argument('--max_new_tokens', type=int, help='sets the number of new tokens to generate when decoding', default=10)
    parser.add_argument('--temperature', type=float, help='generation param that sets the model stability', default=0.5)
    parser.add_argument('--top_k', type=int, default=15)
    parser.add_argument('--top_p', type=float, default=0.7)
    parser.add_argument('--num_return_sequences', type=int, default=1)  
    parser.set_defaults(sample=True)
    
    # Task Type
    parser.add_argument('--task_type', type=str, help='task type to run', default='base_inference', choices=['base_inference', 
    'CoT_inference', 
    'icl_inference_1-shot', 'icl_inference_2-shot', 'icl_inference_CoT-ver_1-shot', 'icl_inference_CoT-ver_2-shot',
    'self-consistency_inference', 'self-consistency_CoT_inference'])

    # ICL Params
    parser.add_argument('--icl_source', type=str, default=f'')

    # Output directory
    parser.add_argument('--output_dir', type=str, help='path to output_dir', default="outputs/")

    # Random Seed
    parser.add_argument('--random_seed', type=int, default= 0)

    args = parser.parse_args()

    # Control Randomness for Reproducibility experiments
    set_random_seed(args.random_seed)

    model = None

    if args.checkpoint != "":
        model = AutoModelForCausalLM.from_pretrained(args.model, device_map= {"": 0}, torch_dtype=torch.bfloat16,attn_implementation="flash_attention_2")
        model = PeftModel.from_pretrained(model, args.checkpoint, device_map= {"": 0}, torch_dtype=torch.bfloat16,attn_implementation="flash_attention_2")
        model = model.merge_and_unload()
        print(f'Merged {args.model=} with {args.checkpoint=}')

    else:
        model = AutoModelForCausalLM.from_pretrained(
            args.model, low_cpu_mem_usage=True,
            return_dict=True, torch_dtype=torch.bfloat16,
            device_map= {"": 0}, attn_implementation="flash_attention_2"
        )

    tokenizer = AutoTokenizer.from_pretrained(args.model) if "llama" not in args.model else AutoTokenizer.from_pretrained(args.model, padding_side="left")
    tokenizer.pad_token_id = tokenizer.eos_token_id


    # Load dataset, queries, qrels and prompts
    queries = json.load(open(args.queries))
    qrels = json.load(open(args.qrels))
    prompt = json.load(open(args.prompt_file))[args.prompt_name]

    #print(f'WARNING: RUNNING 5 SEED ITERATIONS, COMMENT LATER')
    for i in range(1, 6):
        args.random_seed = i
        set_random_seed(args.random_seed)

        output_prompt_labels(model, tokenizer, queries, prompt, args, args.used_set)

    #output_prompt_labels(model, tokenizer, queries, prompt, args, args.used_set)

if __name__ == '__main__':
    main()