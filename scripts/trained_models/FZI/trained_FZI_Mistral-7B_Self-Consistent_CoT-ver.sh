MODEL=mistralai/Mistral-7B-Instruct-v0.2
CHECKPOINT=outputs/models/trained-FZI_Mistral-7B_CoT-ver/checkpoint-980
EXP_NAME=trained_FZI_Mistral-7B_Self-Consistent_CoT-ver_400-Max-Tokens
USED_SET=test
QUERIES=data/SemEval-2024/queries/queries2024_$USED_SET.json
QRELS=data/SemEval-2024/qrels/qrels2024_$USED_SET.json
PROMPT_FILE=src/prompts/FZI_Prompts.json
PROMPT_NAME=FZI_Mistral7B_CoT-ver_prompt
OUTPUT_DIR=outputs/trained_models/FZI/trained_FZI_Mistral-7B_Self-Consistent_CoT-ver_checkpoint-980/
BATCH_SIZE=2
MAX_NEW_TOKENS=400
TEMPERATURE=1.0
TOP_K=50
TOP_P=0.99
NUM_RETURN_SEQUENCES=5
RANDOM_SEED=0

CUDA_VISIBLE_DEVICES=$1 python -m src.inference.inference \
    --model $MODEL\
    --checkpoint $CHECKPOINT \
    --exp_name $EXP_NAME \
    --used_set $USED_SET \
    --queries $QUERIES \
    --qrels $QRELS \
    --prompt_file $PROMPT_FILE \
    --prompt_name $PROMPT_NAME \
    --output_dir $OUTPUT_DIR \
    --task_type self-consistency_CoT_inference \
    --batch_size $BATCH_SIZE \
    --max_new_tokens $MAX_NEW_TOKENS \
    --temperature $TEMPERATURE \
    --top_k $TOP_K \
    --top_p $TOP_P \
    --num_return_sequences $NUM_RETURN_SEQUENCES