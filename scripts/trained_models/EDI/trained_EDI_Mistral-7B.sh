MODEL=mistralai/Mistral-7B-Instruct-v0.2
CHECKPOINT=outputs/models/trained-EDI_Mistral-7B_true-dropout/checkpoint-590
EXP_NAME=trained_EDI_Mistral-7B_true-dropout_checkpoint-590
USED_SET=test
QUERIES=data/SemEval-2024/queries/queries2024_$USED_SET.json
QRELS=data/SemEval-2024/qrels/qrels2024_$USED_SET.json
PROMPT_FILE=src/prompts/EDI_Prompts.json
PROMPT_NAME=EDI_Mistral7B_prompt
OUTPUT_DIR=outputs/trained_models/EDI/trained_EDI_Mistral-7B_true-dropout/
BATCH_SIZE=1
MAX_NEW_TOKENS=100
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
    --task_type base_inference \
    --batch_size $BATCH_SIZE \
    --max_new_tokens $MAX_NEW_TOKENS \
    --random_seed $RANDOM_SEED \
    --no_sample 