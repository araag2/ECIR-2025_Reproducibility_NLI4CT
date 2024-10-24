MODEL=amazon/MistralLite
CHECKPOINT=outputs/models/trained-EDI_MistralLite_true-dropout/checkpoint-66
EXP_NAME=trained_EDI_MistralLite7B_checkpoint-66_Sample
USED_SET=test
QUERIES=data/SemEval-2024/queries/queries2024_$USED_SET.json
QRELS=data/SemEval-2024/qrels/qrels2024_$USED_SET.json
PROMPT_FILE=src/prompts/EDI_Prompts.json
PROMPT_NAME=EDI_MistralLite_prompt
OUTPUT_DIR=outputs/trained_models/EDI/MistralLite7B_checkpoint-66/
BATCH_SIZE=8
MAX_NEW_TOKENS=10
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
    #--no_sample 