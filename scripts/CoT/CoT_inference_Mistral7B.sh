MODEL=mistralai/Mistral-7B-Instruct-v0.2
EXP_NAME=CoT_Mistral-7B
USED_SET=test
QUERIES=data/SemEval-2024/queries/queries2024_$USED_SET.json
QRELS=data/SemEval-2024/qrels/qrels2024_$USED_SET.json
PROMPT_FILE=src/prompts/CoT_Prompts.json
PROMPT_NAME=Mistral7B_CoT-prompt
OUTPUT_DIR=outputs/

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
    --max_new_tokens 300 \
    --no_sample