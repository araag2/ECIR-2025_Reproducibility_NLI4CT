CUDA_VISIBLE_DEVICES=2
MODEL=mistralai/Mistral-7B-Instruct-v0.2
EXP_NAME=baseline_Mistral-7B_zero-shot_short-prompt_No-Sample
USED_SET=test
QUERIES=data/SemEval-2024/queries/queries2024_$USED_SET.json
QRELS=data/SemEval-2024/qrels/qrels2024_$USED_SET.json
PROMPT_FILE=src/prompts/Baseline_Prompts.json
PROMPT_NAME=Mistral7B_short-prompt
OUTPUT_DIR=outputs/

python -m src.inference.baseline_inference \
    --model $MODEL\
    --exp_name $EXP_NAME \
    --used_set $USED_SET \
    --queries $QUERIES \
    --qrels $QRELS \
    --prompt_file $PROMPT_FILE \
    --prompt_name $PROMPT_NAME \
    --no_sample \
    --output_dir $OUTPUT_DIR
