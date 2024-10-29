# Full Evaluation Scores

File name: scores.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                79.0        84.0          69.1        77.4

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.790
Control_Precision: 0.796
Control_Recall: 0.783

## Overall Contrast Score

Contrast_F1: 0.534
Contrast_Precision: 0.510
Contrast_Recall: 0.561
**Official Metric ->** Faithfulness: 0.840
**Official Metric ->** Consistency: 0.691

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.733
Para_Precision: 0.731
Para_Recall: 0.735
Para_Consistency: 0.733


### Numerical Paraphrase

Numerical_Para_F1: 0.507
Numerical_Para_Precision: 0.418
Numerical_Para_Recall: 0.644
Numerical_Para_Consistency: 0.670


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.835
Cont_Consistency: 0.775


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.877
Numerical_Cont_Consistency: 0.914


## Text_Append Scores

Text_Append_F1: 0.421
Text_Append_Precision: 0.300
Text_Append_Recall: 0.703
Text_Append_Consistency: 0.587

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

