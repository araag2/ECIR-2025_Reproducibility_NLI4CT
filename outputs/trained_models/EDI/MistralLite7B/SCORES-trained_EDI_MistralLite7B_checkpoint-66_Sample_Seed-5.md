# Full Evaluation Scores

File name: trained_EDI_MistralLite7B_checkpoint-66_Sample_Seed-5.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                79.3        72.9          70.2        74.2

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.793
Control_Precision: 0.852
Control_Recall: 0.742

## Overall Contrast Score

Contrast_F1: 0.588
Contrast_Precision: 0.657
Contrast_Recall: 0.532
**Official Metric ->** Faithfulness: 0.729
**Official Metric ->** Consistency: 0.702

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.745
Para_Precision: 0.793
Para_Recall: 0.702
Para_Consistency: 0.729


### Numerical Paraphrase

Numerical_Para_F1: 0.596
Numerical_Para_Precision: 0.582
Numerical_Para_Recall: 0.609
Numerical_Para_Consistency: 0.679


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.724
Cont_Consistency: 0.705


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.763
Numerical_Cont_Consistency: 0.821


## Text_Append Scores

Text_Append_F1: 0.612
Text_Append_Precision: 0.529
Text_Append_Recall: 0.726
Text_Append_Consistency: 0.665

---

## Full Arg List

model = amazon/MistralLite
exp_name = trained_EDI_MistralLite7B_checkpoint-66_Sample
checkpoint = outputs/models/trained-EDI_MistralLite_true-dropout/checkpoint-66
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
output_dir = outputs/trained_models/EDI/MistralLite7B_checkpoint-66/
random_seed = 5
timestamp = 2024-10-24_17-09

---
