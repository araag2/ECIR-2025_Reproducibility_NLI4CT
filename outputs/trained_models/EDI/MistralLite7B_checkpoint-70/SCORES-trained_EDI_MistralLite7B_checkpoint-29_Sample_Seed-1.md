# Full Evaluation Scores

File name: trained_EDI_MistralLite7B_checkpoint-29_Sample_Seed-1.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                65.9        1.4          38.8        35.3

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.659
Control_Precision: 0.976
Control_Recall: 0.497

## Overall Contrast Score

Contrast_F1: 0.482
Contrast_Precision: 0.991
Contrast_Recall: 0.319
**Official Metric ->** Faithfulness: 0.014
**Official Metric ->** Consistency: 0.388

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.665
Para_Precision: 0.991
Para_Recall: 0.500
Para_Consistency: 0.500


### Numerical Paraphrase

Numerical_Para_F1: 0.581
Numerical_Para_Precision: 1.000
Numerical_Para_Recall: 0.410
Numerical_Para_Consistency: 0.415


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.016
Cont_Consistency: 0.007


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.000
Numerical_Cont_Consistency: 0.019


## Text_Append Scores

Text_Append_F1: 0.665
Text_Append_Precision: 0.991
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
random_seed = 1
timestamp = 2024-10-22_21-53

---

