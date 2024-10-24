# Full Evaluation Scores

File name: trained_EDI_MistralLite7B_checkpoint-70_Greedy_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                79.3        68.9          69.6        72.6

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.793
Control_Precision: 0.880
Control_Recall: 0.721

## Overall Contrast Score

Contrast_F1: 0.598
Contrast_Precision: 0.713
Contrast_Recall: 0.514
**Official Metric ->** Faithfulness: 0.689
**Official Metric ->** Consistency: 0.696

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.752
Para_Precision: 0.827
Para_Recall: 0.690
Para_Consistency: 0.728


### Numerical Paraphrase

Numerical_Para_F1: 0.606
Numerical_Para_Precision: 0.626
Numerical_Para_Recall: 0.588
Numerical_Para_Consistency: 0.670


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.685
Cont_Consistency: 0.663


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.711
Numerical_Cont_Consistency: 0.809


## Text_Append Scores

Text_Append_F1: 0.650
Text_Append_Precision: 0.611
Text_Append_Recall: 0.695
Text_Append_Consistency: 0.671

---

## Full Arg List

model = amazon/MistralLite
exp_name = trained_EDI_MistralLite7B_checkpoint-70_Greedy
checkpoint = outputs/models/trained-EDI_MistralLite_true-dropout/checkpoint-70
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/EDI_Prompts.json
prompt_name = EDI_MistralLite_prompt
batch_size = 6
sample = False
max_new_tokens = 10
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/trained_models/EDI/MistralLite7B_checkpoint-70/
random_seed = 0
timestamp = 2024-10-24_13-46

---

