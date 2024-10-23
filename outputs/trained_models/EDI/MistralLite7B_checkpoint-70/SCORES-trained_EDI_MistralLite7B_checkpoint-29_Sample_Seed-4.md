# Full Evaluation Scores

File name: trained_EDI_MistralLite7B_checkpoint-29_Sample_Seed-4.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                66.4        2.0          39.0        35.8

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.664
Control_Precision: 0.992
Control_Recall: 0.499

## Overall Contrast Score

Contrast_F1: 0.483
Contrast_Precision: 0.992
Contrast_Recall: 0.320
**Official Metric ->** Faithfulness: 0.020
**Official Metric ->** Consistency: 0.390

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.666
Para_Precision: 0.993
Para_Recall: 0.501
Para_Consistency: 0.503


### Numerical Paraphrase

Numerical_Para_F1: 0.572
Numerical_Para_Precision: 0.978
Numerical_Para_Recall: 0.405
Numerical_Para_Consistency: 0.406


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.021
Cont_Consistency: 0.015


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.009
Numerical_Cont_Consistency: 0.019


## Text_Append Scores

Text_Append_F1: 0.665
Text_Append_Precision: 0.992
Text_Append_Recall: 0.501
Text_Append_Consistency: 0.501

---

## Full Arg List

model = amazon/MistralLite
exp_name = trained_EDI_MistralLite7B_checkpoint-29_Sample
checkpoint = outputs/models/trained-EDI_MistralLite_true-dropout/checkpoint-29
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/EDI_Prompts.json
prompt_name = EDI_MistralLite_prompt
batch_size = 8
sample = True
max_new_tokens = 10
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/trained_models/EDI/MistralLite7B_checkpoint-70/
random_seed = 4
timestamp = 2024-10-22_23-17

---

