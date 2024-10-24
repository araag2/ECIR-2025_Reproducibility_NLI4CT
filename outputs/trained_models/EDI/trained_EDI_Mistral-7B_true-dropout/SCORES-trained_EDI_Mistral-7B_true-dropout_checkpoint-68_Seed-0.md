# Full Evaluation Scores

File name: trained_EDI_Mistral-7B_true-dropout_checkpoint-68_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                79.5        81.7          70.3        77.2

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.795
Control_Precision: 0.800
Control_Recall: 0.791

## Overall Contrast Score

Contrast_F1: 0.526
Contrast_Precision: 0.484
Contrast_Recall: 0.577
**Official Metric ->** Faithfulness: 0.817
**Official Metric ->** Consistency: 0.703

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.748
Para_Precision: 0.739
Para_Recall: 0.757
Para_Consistency: 0.751


### Numerical Paraphrase

Numerical_Para_F1: 0.558
Numerical_Para_Precision: 0.451
Numerical_Para_Recall: 0.732
Numerical_Para_Consistency: 0.710


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.813
Cont_Consistency: 0.785


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.842
Numerical_Cont_Consistency: 0.969


## Text_Append Scores

Text_Append_F1: 0.360
Text_Append_Precision: 0.233
Text_Append_Recall: 0.785
Text_Append_Consistency: 0.585

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_EDI_Mistral-7B_true-dropout_checkpoint-68
checkpoint = outputs/models/trained-EDI_Mistral-7B_true-dropout/checkpoint-68
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/EDI_Prompts.json
prompt_name = EDI_Mistral7B_prompt
batch_size = 6
sample = False
max_new_tokens = 10
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/trained_models/EDI/trained_EDI_Mistral-7B_true-dropout/
random_seed = 0
timestamp = 2024-10-24_15-09

---

