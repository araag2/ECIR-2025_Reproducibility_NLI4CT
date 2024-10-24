# Full Evaluation Scores

File name: trained_EDI_Mistral-7B_true-dropout_checkpoint-76_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                78.7        85.1          70.8        78.2

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.787
Control_Precision: 0.768
Control_Recall: 0.807

## Overall Contrast Score

Contrast_F1: 0.523
Contrast_Precision: 0.461
Contrast_Recall: 0.604
**Official Metric ->** Faithfulness: 0.851
**Official Metric ->** Consistency: 0.708

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.730
Para_Precision: 0.697
Para_Recall: 0.766
Para_Consistency: 0.742


### Numerical Paraphrase

Numerical_Para_F1: 0.569
Numerical_Para_Precision: 0.451
Numerical_Para_Recall: 0.774
Numerical_Para_Consistency: 0.723


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.848
Cont_Consistency: 0.817


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.868
Numerical_Cont_Consistency: 0.988


## Text_Append Scores

Text_Append_F1: 0.354
Text_Append_Precision: 0.227
Text_Append_Recall: 0.806
Text_Append_Consistency: 0.586

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_EDI_Mistral-7B_true-dropout_checkpoint-76
checkpoint = outputs/models/trained-EDI_Mistral-7B_true-dropout/checkpoint-76
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
timestamp = 2024-10-24_14-37

---

