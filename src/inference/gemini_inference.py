import argparse
import json
import torch
import datetime
import random
import base64
import vertexai

from vertexai.generative_models import GenerativeModel, SafetySetting, Part
from .output_labels import output_prompt_labels

def main():
    parser = argparse.ArgumentParser()

    # Model and checkpoint paths
    parser.add_argument('--model', type=str, help='name of the model used to generate and combine prompts', default='')   
    parser.add_argument('--exp_name', type=str, help='name of the experiment', default='')
    parser.add_argument('--project', type=str, help='VertexAI project of the model', default='')
    parser.add_argument('--location', type=str, help='Server Location closer to where we are', default='')

    # Path to queries, qrels and prompt files
    parser.add_argument('--used_set', type=str, help='choose which data to use', default='') # train | dev | test
    args = parser.parse_known_args()

    parser.add_argument('--queries', type=str, help='path to queries file', default=f'')
    parser.add_argument('--qrels', type=str, help='path to qrels file', default=f'')
    
    parser.add_argument('--prompt_file', type=str, help='path to prompts file', default='')
    parser.add_argument('--prompt_name', type=str, help='name of the prompt to use', default='')

    parser.add_argument('--max_new_tokens', type=int, help='sets the number of new tokens to generate when decoding', default=10)
    parser.add_argument('--temperature', type=float, help='generation param that sets the model stability', default=0.5)
    parser.add_argument('--top_k', type=int, default=15)
    parser.add_argument('--top_p', type=float, default=0.7)
    parser.add_argument('--num_return_sequences', type=int, default=1)  
    parser.set_defaults(sample=True)
    
    # Task Type
    parser.add_argument('--task_type', type=str, help='task type to run', default='base_inference', choices=['base_inference', 
    'CoT_inference', 
    'icl_inference_1-shot', 'icl_inference_2-shot', 
    'CoT-ICL_inference', 
    'self-consistency_inference', 'self-consistency_CoT_inference'])
    # ICL Params
    parser.add_argument('--icl_source', type=str, default=f'')

    # Output directory
    parser.add_argument('--output_dir', type=str, help='path to output_dir', default="outputs/")

    # Random Seed
    parser.add_argument('--random_seed', type=int, default= 0)
    args = parser.parse_args()


    # Load dataset, queries, qrels and prompts
    queries = json.load(open(args.queries))
    qrels = json.load(open(args.qrels))
    prompt = json.load(open(args.prompt_file))[args.prompt_name]


    generation_config = {
        "max_output_tokens": args.max_new_tokens,
        "temperature": args.temperature,
        "top_p" : args.top_p,
        "top_k" : args.top_k,
    }

    safety_settings = [
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
        SafetySetting(
            category=SafetySetting.HarmCategory.HARM_CATEGORY_HARASSMENT,
            threshold=SafetySetting.HarmBlockThreshold.OFF
        ),
    ]

    vertexai.init(project=args.project, location=args.location)
    model = GenerativeModel(
        args.model,
    )
    chat = model.start_chat()

    # TO:DO Change how this works for the model at hand
    output_prompt_labels(model, tokenizer, queries, prompt, args, args.used_set)

if __name__ == '__main__':
    main()