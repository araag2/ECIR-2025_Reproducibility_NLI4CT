MODEL=meta-llama/Llama-3.2-3B-Instruct
EXP_NAME=baseline_llama3.2_instruct_zero-shot_long-prompt_Greedy
USED_SET=test
QUERIES=data/SemEval-2024/queries/queries2024_$USED_SET.json
QRELS=data/SemEval-2024/qrels/qrels2024_$USED_SET.json
PROMPT_FILE=src/prompts/Baseline_Prompts.json
PROMPT_NAME=llama_long-prompt
OUTPUT_DIR=outputs/

CUDA_VISIBLE_DEVICES=$1 python -m src.inference.baseline_inference \
    --model $MODEL\
    --exp_name $EXP_NAME \
    --used_set $USED_SET \
    --queries $QUERIES \
    --qrels $QRELS \
    --prompt_file $PROMPT_FILE \
    --prompt_name $PROMPT_NAME \
    --no_sample \
    --output_dir $OUTPUT_DIR