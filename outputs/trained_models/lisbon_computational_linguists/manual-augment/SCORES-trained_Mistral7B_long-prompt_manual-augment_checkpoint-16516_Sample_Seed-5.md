# Full Evaluation Scores

File name: trained_Mistral7B_long-prompt_manual-augment_checkpoint-16516_Sample_Seed-5.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                77.5        82.5          70.1        76.7

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.775
Control_Precision: 0.764
Control_Recall: 0.786

## Overall Contrast Score

Contrast_F1: 0.521
Contrast_Precision: 0.475
Contrast_Recall: 0.577
**Official Metric ->** Faithfulness: 0.825
**Official Metric ->** Consistency: 0.701

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.756
Para_Precision: 0.757
Para_Recall: 0.754
Para_Consistency: 0.755


### Numerical Paraphrase

Numerical_Para_F1: 0.609
Numerical_Para_Precision: 0.505
Numerical_Para_Recall: 0.767
Numerical_Para_Consistency: 0.737


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.815
Cont_Consistency: 0.780


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.895
Numerical_Cont_Consistency: 0.951


## Text_Append Scores

Text_Append_F1: 0.308
Text_Append_Precision: 0.189
Text_Append_Recall: 0.821
Text_Append_Consistency: 0.574

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_Mistral7B_long-prompt_manual-augment_checkpoint-16516_Sample
checkpoint = outputs/models/baseline_Mistral-7B_training_short-prompt_manual-augment/checkpoint-16516
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/Baseline_Prompts.json
prompt_name = Mistral7B_short-prompt
batch_size = 16
sample = True
max_new_tokens = 2
temperature = 1.0
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/trained_models/lisbon_computational_linguists/manual-augment/
random_seed = 5
timestamp = 2024-10-22_21-03

---
