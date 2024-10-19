# Full Evaluation Scores

File name: trained_FZI_Mistral-7B_CoT-ver_Greedy_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                66.0        39.1          51.2        52.1

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.660
Control_Precision: 0.804
Control_Recall: 0.560

## Overall Contrast Score

Contrast_F1: 0.476
Contrast_Precision: 0.727
Contrast_Recall: 0.354
**Official Metric ->** Faithfulness: 0.391
**Official Metric ->** Consistency: 0.512

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.659
Para_Precision: 0.821
Para_Recall: 0.550
Para_Consistency: 0.575


### Numerical Paraphrase

Numerical_Para_F1: 0.509
Numerical_Para_Precision: 0.637
Numerical_Para_Recall: 0.423
Numerical_Para_Consistency: 0.500


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.381
Cont_Consistency: 0.391


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.456
Numerical_Cont_Consistency: 0.481


## Text_Append Scores

Text_Append_F1: 0.570
Text_Append_Precision: 0.643
Text_Append_Recall: 0.512
Text_Append_Consistency: 0.515

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_FZI_Mistral-7B_CoT-ver_Greedy
checkpoint = outputs/models/trained-FZI_Mistral-7B_CoT-ver/checkpoint-980
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/FZI_Prompts.json
prompt_name = FZI_Mistral7B_CoT-ver_prompt
batch_size = 1
sample = False
max_new_tokens = 1000
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = CoT_inference
icl_source = 
output_dir = outputs/trained_models/FZI/trained_FZI_Mistral-7B_CoT-ver/
random_seed = 0
timestamp = 2024-10-19_11-04

---

