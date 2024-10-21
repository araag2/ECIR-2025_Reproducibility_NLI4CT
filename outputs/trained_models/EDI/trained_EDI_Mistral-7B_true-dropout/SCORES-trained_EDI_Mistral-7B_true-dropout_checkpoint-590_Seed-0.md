# Full Evaluation Scores

File name: trained_EDI_Mistral-7B_true-dropout_checkpoint-590_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                55.7        38.0          47.0        46.9

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.557
Control_Precision: 0.624
Control_Recall: 0.503

## Overall Contrast Score

Contrast_F1: 0.423
Contrast_Precision: 0.629
Contrast_Recall: 0.319
**Official Metric ->** Faithfulness: 0.380
**Official Metric ->** Consistency: 0.470

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.561
Para_Precision: 0.621
Para_Recall: 0.511
Para_Consistency: 0.513


### Numerical Paraphrase

Numerical_Para_F1: 0.533
Numerical_Para_Precision: 0.703
Numerical_Para_Recall: 0.430
Numerical_Para_Consistency: 0.500


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.376
Cont_Consistency: 0.373


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.404
Numerical_Cont_Consistency: 0.364


## Text_Append Scores

Text_Append_F1: 0.547
Text_Append_Precision: 0.628
Text_Append_Recall: 0.485
Text_Append_Consistency: 0.481

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_EDI_Mistral-7B_true-dropout_checkpoint-590
checkpoint = outputs/models/trained-EDI_Mistral-7B_true-dropout/checkpoint-590
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/EDI_Prompts.json
prompt_name = EDI_Mistral7B_prompt
batch_size = 1
sample = False
max_new_tokens = 100
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/trained_models/EDI/trained_EDI_Mistral-7B_true-dropout/
random_seed = 0
timestamp = 2024-10-21_02-48

---

