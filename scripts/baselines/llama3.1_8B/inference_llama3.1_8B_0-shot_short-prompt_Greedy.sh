MODEL=meta-llama/Llama-3.1-8B-Instruct
EXP_NAME=baseline_llama3.1-8B_0-shot_short-prompt_Greedy
USED_SET=test
QUERIES=data/SemEval-2024/queries/queries2024_$USED_SET.json
QRELS=data/SemEval-2024/qrels/qrels2024_$USED_SET.json
PROMPT_FILE=src/prompts/Baseline_Prompts.json
PROMPT_NAME=llama_short-prompt
OUTPUT_DIR=outputs/paper_baselines/llama3.1-8B/llama3.1-8B_0-shot_short-prompt_Greedy/
BATCH_SIZE=1
MAX_NEW_TOKENS=10
SEED=0

CUDA_VISIBLE_DEVICES=$1 python -m src.inference.inference \
    --model $MODEL\
    --exp_name $EXP_NAME \
    --used_set $USED_SET \
    --queries $QUERIES \
    --qrels $QRELS \
    --prompt_file $PROMPT_FILE \
    --prompt_name $PROMPT_NAME \
    --output_dir $OUTPUT_DIR \
    --task_type base_inference \
    --batch_size $BATCH_SIZE \
    --max_new_tokens $MAX_NEW_TOKENS \
    --random_seed $SEED \
    --no_sample