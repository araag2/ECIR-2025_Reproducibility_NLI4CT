# Full Evaluation Scores

File name: trained_FZI_Mistral-7B_label-only_Greedy_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                62.9        44.9          55.5        54.4

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.629
Control_Precision: 0.732
Control_Recall: 0.551

## Overall Contrast Score

Contrast_F1: 0.487
Contrast_Precision: 0.692
Contrast_Recall: 0.376
**Official Metric ->** Faithfulness: 0.449
**Official Metric ->** Consistency: 0.555

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.628
Para_Precision: 0.731
Para_Recall: 0.551
Para_Consistency: 0.567


### Numerical Paraphrase

Numerical_Para_F1: 0.531
Numerical_Para_Precision: 0.560
Numerical_Para_Recall: 0.505
Numerical_Para_Consistency: 0.598


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.432
Cont_Consistency: 0.481


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.561
Numerical_Cont_Consistency: 0.611


## Text_Append Scores

Text_Append_F1: 0.608
Text_Append_Precision: 0.669
Text_Append_Recall: 0.557
Text_Append_Consistency: 0.568

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_FZI_Mistral-7B_label-only_Greedy
checkpoint = outputs/models/trained-FZI_Mistral-7B_label-only/checkpoint-1185
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/FZI_Prompts.json
prompt_name = FZI_Mistral7B_label-only_prompt
batch_size = 1
sample = False
max_new_tokens = 100
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/trained_models/FZI/trained_FZI_Mistral-7B_label-only/
random_seed = 0
timestamp = 2024-10-19_07-30

---

