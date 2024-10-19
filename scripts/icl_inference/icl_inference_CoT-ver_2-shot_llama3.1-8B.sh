MODEL=meta-llama/Llama-3.1-8B-Instruct
EXP_NAME=icl_CoT-ver_2-shot_llama3.1-8B
USED_SET=test
QUERIES=data/SemEval-2024/queries/queries2024_$USED_SET.json
QRELS=data/SemEval-2024/qrels/qrels2024_$USED_SET.json
ICL_SOURCE=data/SemEval-2024/icl/icl_CoT-ver/icl_CoT-ver_EDI_GPT-4_llama3.1-8B.json
PROMPT_FILE=src/prompts/ICL_Prompts.json
PROMPT_NAME=icl-2_EDI-CoT-ver_llama3.1-8B_prompt
OUTPUT_DIR=outputs/icl_CoT-ver_2-shot/
BATCH_SIZE=1
MAX_NEW_TOKENS=1000
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
    --task_type icl_inference_CoT-ver_2-shot \
    --icl_source $ICL_SOURCE \
    --batch_size $BATCH_SIZE \
    --max_new_tokens $MAX_NEW_TOKENS \
    --random_seed $RANDOM_SEED \
    --no_sample