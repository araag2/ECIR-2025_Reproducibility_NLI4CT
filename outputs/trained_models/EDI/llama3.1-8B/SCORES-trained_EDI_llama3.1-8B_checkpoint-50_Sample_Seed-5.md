# Full Evaluation Scores

File name: trained_EDI_llama3.1-8B_checkpoint-50_Sample_Seed-5.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                80.9        72.7          73.5        75.7

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.809
Control_Precision: 0.872
Control_Recall: 0.754

## Overall Contrast Score

Contrast_F1: 0.621
Contrast_Precision: 0.687
Contrast_Recall: 0.567
**Official Metric ->** Faithfulness: 0.727
**Official Metric ->** Consistency: 0.735

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.795
Para_Precision: 0.844
Para_Recall: 0.752
Para_Consistency: 0.783


### Numerical Paraphrase

Numerical_Para_F1: 0.701
Numerical_Para_Precision: 0.747
Numerical_Para_Recall: 0.660
Numerical_Para_Consistency: 0.741


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.737
Cont_Consistency: 0.708


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.658
Numerical_Cont_Consistency: 0.864


## Text_Append Scores

Text_Append_F1: 0.624
Text_Append_Precision: 0.523
Text_Append_Recall: 0.773
Text_Append_Consistency: 0.685

---

## Full Arg List

model = meta-llama/Llama-3.1-8B-Instruct
exp_name = trained_EDI_llama3.1-8B_checkpoint-50_Sample
checkpoint = outputs/models/trained-EDI_llama3.1-8B/checkpoint-50
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/EDI_Prompts.json
prompt_name = EDI_llama-prompt
batch_size = 8
sample = True
max_new_tokens = 2
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/trained_models/EDI/llama3.1-8B_checkpoint-50/
random_seed = 5
timestamp = 2024-10-22_19-44

---

