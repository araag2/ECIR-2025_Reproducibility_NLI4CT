MODEL=mistralai/Mixtral-8x7B-Instruct-v0.1
TOKENIZER=mistralai/Mixtral-8x7B-Instruct-v0.1
#MERGE
CHECKPOINT=None
EXP_NAME=FZI-WIM_Mixtral-8x7B_training
RUN=2
SAVE_DIR=outputs/models/
TRAIN_DATA=data/SemEval-2024/training_preprocessed_data/Preprocessed-Data_train-set.json
EVAL_DATA=data/SemEval-2024/training_preprocessed_data/Preprocessed-Data_dev-set.json
TASK_TYPE=base
#Hyperparameters Config
MAX_LENGTH=2000
BATCH_SIZE=1
POOLING=mean
TRAIN_EPOCHS=5
LR=1e-5
LORA_R=8
LORA_DROPOUT=0.0
LORA_ALPHA=32

CUDA_VISIBLE_DEVICES=$1 python -m src.training.baseline_training \
    --model_name $MODEL \
    --tokenizer_name $TOKENIZER \
    --no-merge \
    --checkpoint $CHECKPOINT \
    --exp_name $EXP_NAME \
    --run $RUN \
    --save_dir $SAVE_DIR \
    --train_data $TRAIN_DATA \
    --eval_data $EVAL_DATA \
    --task_type $TASK_TYPE \
    --max_length $MAX_LENGTH \
    --batch_size $BATCH_SIZE \
    --pooling $POOLING \
    --train_epochs $TRAIN_EPOCHS \
    --lr $LR \
    --lora_r $LORA_R \
    --lora_dropout $LORA_DROPOUT \
    --lora_alpha $LORA_ALPHA \