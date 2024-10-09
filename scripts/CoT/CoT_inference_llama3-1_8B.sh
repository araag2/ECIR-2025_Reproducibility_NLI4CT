MODEL=meta-llama/Llama-3.1-8B-Instruct
EXP_NAME=CoT_llama3.1-8B
USED_SET=test
QUERIES=data/SemEval-2024/queries/queries2024_$USED_SET.json
QRELS=data/SemEval-2024/qrels/qrels2024_$USED_SET.json
PROMPT_FILE=src/prompts/CoT_Prompts.json
PROMPT_NAME=llama_CoT-prompt
OUTPUT_DIR=outputs/
MAX_NEW_TOKENS=1000

CUDA_VISIBLE_DEVICES=$1 python -m src.inference.inference \
    --model $MODEL\
    --exp_name $EXP_NAME \
    --used_set $USED_SET \
    --queries $QUERIES \
    --qrels $QRELS \
    --prompt_file $PROMPT_FILE \
    --prompt_name $PROMPT_NAME \
    --output_dir $OUTPUT_DIR \
    --task_type CoT_inference \
    --max_new_tokens $MAX_NEW_TOKENS \
    --no_sample