# Full Evaluation Scores

File name: trained_EDI_Mistral-7B_true-dropout_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                58.1        34.3          45.4        45.9

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.581
Control_Precision: 0.688
Control_Recall: 0.503

## Overall Contrast Score

Contrast_F1: 0.419
Contrast_Precision: 0.640
Contrast_Recall: 0.311
**Official Metric ->** Faithfulness: 0.343
**Official Metric ->** Consistency: 0.454

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.563
Para_Precision: 0.645
Para_Recall: 0.500
Para_Consistency: 0.500


### Numerical Paraphrase

Numerical_Para_F1: 0.524
Numerical_Para_Precision: 0.714
Numerical_Para_Recall: 0.414
Numerical_Para_Consistency: 0.473


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.356
Cont_Consistency: 0.343


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.254
Numerical_Cont_Consistency: 0.247


## Text_Append Scores

Text_Append_F1: 0.548
Text_Append_Precision: 0.625
Text_Append_Recall: 0.487
Text_Append_Consistency: 0.483

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_EDI_Mistral-7B_true-dropout
checkpoint = outputs/models/trained-EDI_Mistral-7B_true-dropout/checkpoint-590
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/Baseline_Prompts.json
prompt_name = Mistral7B_short-prompt
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
timestamp = 2024-10-21_03-13

---

