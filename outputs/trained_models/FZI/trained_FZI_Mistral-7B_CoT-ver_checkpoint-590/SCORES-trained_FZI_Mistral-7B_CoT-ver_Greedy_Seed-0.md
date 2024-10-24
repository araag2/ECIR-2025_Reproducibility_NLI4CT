# Full Evaluation Scores

File name: trained_FZI_Mistral-7B_CoT-ver_Greedy_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                49.0        85.9          63.4        66.1

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.490
Control_Precision: 0.384
Control_Recall: 0.676

## Overall Contrast Score

Contrast_F1: 0.359
Contrast_Precision: 0.288
Contrast_Recall: 0.476
**Official Metric ->** Faithfulness: 0.859
**Official Metric ->** Consistency: 0.634

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.473
Para_Precision: 0.373
Para_Recall: 0.645
Para_Consistency: 0.584


### Numerical Paraphrase

Numerical_Para_F1: 0.385
Numerical_Para_Precision: 0.286
Numerical_Para_Recall: 0.591
Numerical_Para_Consistency: 0.629


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.861
Cont_Consistency: 0.863


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.842
Numerical_Cont_Consistency: 0.858


## Text_Append Scores

Text_Append_F1: 0.310
Text_Append_Precision: 0.204
Text_Append_Recall: 0.643
Text_Append_Consistency: 0.545

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_FZI_Mistral-7B_CoT-ver_Greedy
checkpoint = outputs/models/trained-FZI_Mistral-7B_CoT-ver/checkpoint-590
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/FZI_Prompts.json
prompt_name = FZI_Mistral7B_CoT-ver_prompt
batch_size = 32
sample = False
max_new_tokens = 250
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = CoT_inference
icl_source = 
output_dir = outputs/trained_models/FZI/trained_FZI_Mistral-7B_CoT-ver_checkpoint-590/
random_seed = 0
timestamp = 2024-10-24_04-22

---

