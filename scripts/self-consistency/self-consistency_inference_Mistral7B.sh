MODEL=mistralai/Mistral-7B-Instruct-v0.2
EXP_NAME=self-consistency_Mistral-7B
USED_SET=test
QUERIES=data/SemEval-2024/queries/queries2024_$USED_SET.json
QRELS=data/SemEval-2024/qrels/qrels2024_$USED_SET.json
PROMPT_FILE=src/prompts/self-consistency_prompts.json
PROMPT_NAME=Mistral7B
OUTPUT_DIR=outputs/self-consistency/Mistral-7B/
BATCH_SIZE=1
MAX_NEW_TOKENS=10
TEMPERATURE=1.0
TOP_K=50
TOP_P=1.0
NUM_RETURN_SEQUENCES=10
RANDOM_SEED=0

CUDA_VISIBLE_DEVICES=$1 python -m src.inference.inference \
    --model $MODEL\
    --exp_name $EXP_NAME \
    --used_set $USED_SET \
    --queries $QUERIES \
    --qrels $QRELS \
    --prompt_file $PROMPT_FILE \
    --prompt_name $PROMPT_NAME \
    --output_dir $OUTPUT_DIR \
    --task_type self-consistency_inference \
    --batch_size $BATCH_SIZE \
    --max_new_tokens $MAX_NEW_TOKENS \
    --temperature $TEMPERATURE \
    --top_k $TOP_K \
    --top_p $TOP_P \
    --num_return_sequences $NUM_RETURN_SEQUENCES \
    --random_seed $RANDOM_SEED \