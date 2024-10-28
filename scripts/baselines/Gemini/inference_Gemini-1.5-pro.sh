MODEL=gemini-1.5-pro-001
EXP_NAME=baseline_Gemini-pro_0-shot_short-prompt_Greedy
PROJECT=stone-passage-376622
LOCATION=europe-central2
USED_SET=test
QUERIES=data/SemEval-2024/queries/queries2024_$USED_SET.json
PROMPT_FILE=src/prompts/Baseline_Prompts.json
PROMPT_NAME=Mistral7B_short-prompt
OUTPUT_DIR=outputs/paper_baselines/Gemini/Gemini-pro_0-shot_short-prompt_Greedy/
BATCH_SIZE=1
MAX_NEW_TOKENS=10
TEMPERATURE=0.01
TOP_K=40
TOP_P=0.99
RANDOM_SEED=0

CUDA_VISIBLE_DEVICES=$1 python -m src.inference.gemini_inference \
    --model $MODEL\
    --exp_name $EXP_NAME \
    --project $PROJECT \
    --location $LOCATION \
    --used_set $USED_SET \
    --queries $QUERIES \
    --prompt_file $PROMPT_FILE \
    --prompt_name $PROMPT_NAME \
    --output_dir $OUTPUT_DIR \
    --task_type base_inference \
    --batch_size $BATCH_SIZE \
    --max_new_tokens $MAX_NEW_TOKENS \
    --temperature $TEMPERATURE \
    --top_k $TOP_K \
    --top_p $TOP_P \
    --random_seed $RANDOM_SEED 