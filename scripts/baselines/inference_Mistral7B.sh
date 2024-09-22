CUDA_VISIBLE_DEVICES=$1
MODEL=mistralai/Mistral-7B-Instruct-v0.2
EXP_NAME=baseline_Mistral-7B_zero-shot
USED_SET=test
QUERIES=data/SemEval-2024/queries/queries2024_$USED_SET.json
QRELS=data/SemEval-2024/qrels/qrels2024_$USED_SET.json
PROMPT_FILE=src/prompts/BaselinePrompts.json
PROMPT_NAME=long_prompt
OUTPUT_DIR=outputs/

CUDA_VISIBLE_DEVICES=1 python -m src.inference.baseline_inference \
    --model $MODEL\
    --exp_name $EXP_NAME \
    --used_set $USED_SET \
    --queries $QUERIES \
    --qrels $QRELS \
    --prompt_file $PROMPT_FILE \
    --prompt_name $PROMPT_NAME \
    --output_dir $OUTPUT_DIR