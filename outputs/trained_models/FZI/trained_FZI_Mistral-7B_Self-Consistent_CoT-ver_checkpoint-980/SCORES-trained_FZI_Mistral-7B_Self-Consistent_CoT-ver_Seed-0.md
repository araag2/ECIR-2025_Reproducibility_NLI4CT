# Full Evaluation Scores

File name: trained_FZI_Mistral-7B_Self-Consistent_CoT-ver_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                75.6        83.3          69.3        76.1

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.756
Control_Precision: 0.756
Control_Recall: 0.756

## Overall Contrast Score

Contrast_F1: 0.544
Contrast_Precision: 0.530
Contrast_Recall: 0.559
**Official Metric ->** Faithfulness: 0.833
**Official Metric ->** Consistency: 0.693

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.719
Para_Precision: 0.712
Para_Recall: 0.727
Para_Consistency: 0.722


### Numerical Paraphrase

Numerical_Para_F1: 0.463
Numerical_Para_Precision: 0.374
Numerical_Para_Recall: 0.607
Numerical_Para_Consistency: 0.647


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.828
Cont_Consistency: 0.789


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.868
Numerical_Cont_Consistency: 0.895


## Text_Append Scores

Text_Append_F1: 0.479
Text_Append_Precision: 0.367
Text_Append_Recall: 0.689
Text_Append_Consistency: 0.601

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_FZI_Mistral-7B_Self-Consistent_CoT-ver
checkpoint = outputs/models/trained-FZI_Mistral-7B_CoT-ver/checkpoint-980
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/FZI_Prompts.json
prompt_name = FZI_Mistral7B_CoT-ver_prompt
batch_size = 2
sample = True
max_new_tokens = 200
temperature = 1.0
top_k = 50
top_p = 0.99
num_return_sequences = 5
task_type = self-consistency_CoT_inference
icl_source = 
output_dir = outputs/trained_models/FZI/trained_FZI_Mistral-7B_Self-Consistent_CoT-ver_checkpoint-980/
random_seed = 0
timestamp = 2024-10-25_05-29

---

