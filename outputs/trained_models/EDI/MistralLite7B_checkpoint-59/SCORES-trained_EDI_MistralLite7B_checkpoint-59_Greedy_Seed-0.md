# Full Evaluation Scores

File name: trained_EDI_MistralLite7B_checkpoint-59_Greedy_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                76.5        56.8          65.7        66.3

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.765
Control_Precision: 0.936
Control_Recall: 0.646

## Overall Contrast Score

Contrast_F1: 0.605
Contrast_Precision: 0.860
Contrast_Recall: 0.466
**Official Metric ->** Faithfulness: 0.568
**Official Metric ->** Consistency: 0.657

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.753
Para_Precision: 0.920
Para_Recall: 0.637
Para_Consistency: 0.698


### Numerical Paraphrase

Numerical_Para_F1: 0.624
Numerical_Para_Precision: 0.758
Numerical_Para_Recall: 0.531
Numerical_Para_Consistency: 0.629


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.561
Cont_Consistency: 0.540


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.614
Numerical_Cont_Consistency: 0.728


## Text_Append Scores

Text_Append_F1: 0.713
Text_Append_Precision: 0.813
Text_Append_Recall: 0.634
Text_Append_Consistency: 0.672

---

## Full Arg List

model = amazon/MistralLite
exp_name = trained_EDI_MistralLite7B_checkpoint-59_Greedy
checkpoint = outputs/models/trained-EDI_MistralLite_true-dropout/checkpoint-59
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
output_dir = outputs/trained_models/EDI/MistralLite7B_checkpoint-59/
random_seed = 0
timestamp = 2024-10-24_15-03

---

