# Full Evaluation Scores

File name: trained_EDI_Mistral-7B_true-dropout_checkpoint-296_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                65.9        1.0          39.1        35.3

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.659
Control_Precision: 0.976
Control_Recall: 0.497

## Overall Contrast Score

Contrast_F1: 0.481
Contrast_Precision: 0.984
Contrast_Recall: 0.318
**Official Metric ->** Faithfulness: 0.010
**Official Metric ->** Consistency: 0.391

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.663
Para_Precision: 0.983
Para_Recall: 0.500
Para_Consistency: 0.501


### Numerical Paraphrase

Numerical_Para_F1: 0.568
Numerical_Para_Precision: 0.967
Numerical_Para_Recall: 0.402
Numerical_Para_Consistency: 0.402


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.011
Cont_Consistency: 0.028


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.009
Numerical_Cont_Consistency: 0.012


## Text_Append Scores

Text_Append_F1: 0.664
Text_Append_Precision: 0.987
Text_Append_Recall: 0.501
Text_Append_Consistency: 0.501

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_EDI_Mistral-7B_true-dropout_checkpoint-296
checkpoint = outputs/models/trained-EDI_Mistral-7B_true-dropout/checkpoint-296
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
timestamp = 2024-10-21_17-33

---

