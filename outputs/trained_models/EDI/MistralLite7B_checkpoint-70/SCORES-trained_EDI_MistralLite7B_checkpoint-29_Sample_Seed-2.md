# Full Evaluation Scores

File name: trained_EDI_MistralLite7B_checkpoint-29_Sample_Seed-2.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                66.3        0.6          38.7        35.2

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.663
Control_Precision: 0.980
Control_Recall: 0.501

## Overall Contrast Score

Contrast_F1: 0.482
Contrast_Precision: 0.991
Contrast_Recall: 0.318
**Official Metric ->** Faithfulness: 0.006
**Official Metric ->** Consistency: 0.387

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.664
Para_Precision: 0.989
Para_Recall: 0.500
Para_Consistency: 0.499


### Numerical Paraphrase

Numerical_Para_F1: 0.580
Numerical_Para_Precision: 1.000
Numerical_Para_Recall: 0.408
Numerical_Para_Consistency: 0.411


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.005
Cont_Consistency: 0.012


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.009
Numerical_Cont_Consistency: 0.000


## Text_Append Scores

Text_Append_F1: 0.665
Text_Append_Precision: 0.991
Text_Append_Recall: 0.500
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
random_seed = 2
timestamp = 2024-10-22_22-21

---

