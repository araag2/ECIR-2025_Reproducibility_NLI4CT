MODEL=amazon/MistralLite
TOKENIZER=amazon/MistralLite
#MERGE
CHECKPOINT=None
EXP_NAME=trained-EDI_MistralLite_EDI_prompt
RUN=1
SAVE_DIR=outputs/models/trained-EDI_MistralLite_true-dropout/
TRAIN_DATA=data/SemEval-2024/training_preprocessed_data/EDI/train_EDI_label-only_train_MistralLite.json
EVAL_DATA=data/SemEval-2024/training_preprocessed_data/EDI/train_EDI_label_only_dev_MistralLite.json
TASK_TYPE=base
#Hyperparameters Config
MAX_LENGTH=4000
BATCH_SIZE=8
POOLING=mean
TRAIN_EPOCHS=10
GRADIENT_ACCUMULATION_STEPS=32
LR=1e-4
WEIGHT_DECAY=0.01
LORA_R=16
LORA_DROPOUT=0.0
LORA_ALPHA=32
LM_TOKEN=Answer: 

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
    --gradient_accumulation_steps $GRADIENT_ACCUMULATION_STEPS \
    --lr $LR \
    --weight_decay $WEIGHT_DECAY \
    --lora_r $LORA_R \
    --lora_dropout $LORA_DROPOUT \
    --lora_alpha $LORA_ALPHA \
    --LM_Token $LM_TOKEN