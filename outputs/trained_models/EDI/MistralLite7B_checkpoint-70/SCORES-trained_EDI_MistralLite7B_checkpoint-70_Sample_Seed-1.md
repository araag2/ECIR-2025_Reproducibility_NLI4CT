# Full Evaluation Scores

File name: trained_EDI_MistralLite7B_checkpoint-70_Sample_Seed-1.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                66.7        0.0          38.5        35.0

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.667
Control_Precision: 1.000
Control_Recall: 0.500

## Overall Contrast Score

Contrast_F1: 0.483
Contrast_Precision: 1.000
Contrast_Recall: 0.318
**Official Metric ->** Faithfulness: 0.000
**Official Metric ->** Consistency: 0.385

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.667
Para_Precision: 1.000
Para_Recall: 0.500
Para_Consistency: 0.500


### Numerical Paraphrase

Numerical_Para_F1: 0.578
Numerical_Para_Precision: 1.000
Numerical_Para_Recall: 0.406
Numerical_Para_Consistency: 0.406


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.000
Cont_Consistency: 0.000


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.000
Numerical_Cont_Consistency: 0.000


## Text_Append Scores

Text_Append_F1: 0.667
Text_Append_Precision: 1.000
Text_Append_Recall: 0.500
Text_Append_Consistency: 0.500

---

## Full Arg List

model = amazon/MistralLite
exp_name = trained_EDI_MistralLite7B_checkpoint-70_Sample
checkpoint = outputs/models/trained-EDI_MistralLite_true-dropout/checkpoint-70
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/EDI_Prompts.json
prompt_name = EDI_MistralLite_prompt
batch_size = 8
sample = True
max_new_tokens = 2
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/trained_models/EDI/MistralLite7B_checkpoint-70/
random_seed = 1
timestamp = 2024-10-22_20-14

---

