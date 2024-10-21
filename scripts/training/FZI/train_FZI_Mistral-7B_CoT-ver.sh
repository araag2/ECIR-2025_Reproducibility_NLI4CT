MODEL=mistralai/Mistral-7B-Instruct-v0.2
TOKENIZER=mistralai/Mistral-7B-Instruct-v0.2
#MERGE
CHECKPOINT=None
EXP_NAME=trained-FZI_Mistral-7B_CoT-ver
RUN=0
SAVE_DIR=outputs/models/trained-FZI_Mistral-7B_CoT-ver/
TRAIN_DATA=data/SemEval-2024/training_preprocessed_data/FZI/train_FZI_CoT-ver.json
TASK_TYPE=base
#Hyperparameters Config
MAX_LENGTH=7000
BATCH_SIZE=16
POOLING=mean
TRAIN_EPOCHS=5
GRADIENT_ACCUMULATION_STEPS=8
LR=1e-4
WEIGHT_DECAY=0.00
LORA_R=8
LORA_DROPOUT=0.0
LORA_ALPHA=32
LM_TOKEN="step: "

CUDA_VISIBLE_DEVICES=$1 python -m src.training.baseline_training \
    --model_name $MODEL \
    --tokenizer_name $TOKENIZER \
    --no-merge \
    --checkpoint $CHECKPOINT \
    --exp_name $EXP_NAME \
    --run $RUN \
    --save_dir $SAVE_DIR \
    --train_data $TRAIN_DATA \
    --task_type $TASK_TYPE \
    --max_length $MAX_LENGTH \
    --batch_size $BATCH_SIZE \
    --pooling $POOLING \
    --train_epochs $TRAIN_EPOCHS \
    --gradient_accumulation_steps $GRADIENT_ACCUMULATION_STEPS \
    --lr $LR \
    --weight_decay $WEIGHT_DECAY \
    --lora_r $LORA_R \
    --lora_dropout $LORA_DROPOUT \
    --lora_alpha $LORA_ALPHA \
    --LM_Token $LM_TOKEN