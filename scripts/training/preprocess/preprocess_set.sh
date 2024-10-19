USED_SET=train-full-synthetic-expand
QUERIES=data/SemEval-2024/data_augmentation/lisbon_computational_linguists/
QRELS=data/SemEval-2024/data_augmentation/lisbon_computational_linguists/
PROMPT_FILE=src/prompts/Baseline_Prompts.json
PROMPT_NAME=Mistral7B_long-prompt
OUTPUT_DIR=data/SemEval-2024/training_preprocessed_data/lisbon_computational_linguists/


python -m src.utils.preprocess_dataset \
    --used_set $USED_SET \
    --queries $QUERIES \
    --qrels $QRELS \
    --prompt_file $PROMPT_FILE \
    --prompt_name $PROMPT_NAME \
    --output_dir $OUTPUT_DIR