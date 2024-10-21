MODEL=mistralai/Mistral-7B-Instruct-v0.2
CHECKPOINT=outputs/models/baseline_Mistral-7B_training_long-prompt_manual-augment/checkpoint-4658
EXP_NAME=trained_Mistral7B_long-prompt_manual-augment_checkpoint-4658
USED_SET=test
QUERIES=data/SemEval-2024/queries/queries2024_$USED_SET.json
QRELS=data/SemEval-2024/qrels/qrels2024_$USED_SET.json
PROMPT_FILE=src/prompts/Baseline_Prompts.json
PROMPT_NAME=Mistral7B_short-prompt
OUTPUT_DIR=outputs/trained_models/lisbon_computational_linguists/manual-augment/
BATCH_SIZE=8
MAX_NEW_TOKENS=25
TEMPERATURE=1.0
TOP_K=15
TOP_P=0.7
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
    --temperature $TEMPERATURE \
    --top_k $TOP_K \
    --top_p $TOP_P \
    --random_seed $RANDOM_SEED \
    --no_sample \