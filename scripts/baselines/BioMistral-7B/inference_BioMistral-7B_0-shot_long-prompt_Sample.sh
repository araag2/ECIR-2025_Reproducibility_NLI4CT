MODEL=BioMistral/BioMistral-7B-DARE
EXP_NAME=baseline_BioMistral-7B_0-shot_long-prompt_Sample
USED_SET=test
QUERIES=data/SemEval-2024/queries/queries2024_$USED_SET.json
QRELS=data/SemEval-2024/qrels/qrels2024_$USED_SET.json
PROMPT_FILE=src/prompts/Baseline_Prompts.json
PROMPT_NAME=Mistral7B_long-prompt
OUTPUT_DIR=outputs/
BATCH_SIZE=1
MAX_NEW_TOKENS=10
TEMPERATURE=0.7
TOP_K=50
TOP_P=0.99
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
    --temperature $TEMPERATURE \
    --top_k $TOP_K \
    --top_p $TOP_P \
    --random_seed $SEED 