# Full Evaluation Scores

File name: trained_FZI_Mistral-7B_label-only_Greedy_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                79.5        78.9          70.3        76.3

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.795
Control_Precision: 0.792
Control_Recall: 0.798

## Overall Contrast Score

Contrast_F1: 0.534
Contrast_Precision: 0.508
Contrast_Recall: 0.563
**Official Metric ->** Faithfulness: 0.789
**Official Metric ->** Consistency: 0.703

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.758
Para_Precision: 0.755
Para_Recall: 0.762
Para_Consistency: 0.759


### Numerical Paraphrase

Numerical_Para_F1: 0.507
Numerical_Para_Precision: 0.407
Numerical_Para_Recall: 0.673
Numerical_Para_Consistency: 0.679


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.784
Cont_Consistency: 0.769


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.825
Numerical_Cont_Consistency: 0.938


## Text_Append Scores

Text_Append_F1: 0.402
Text_Append_Precision: 0.275
Text_Append_Recall: 0.752
Text_Append_Consistency: 0.592

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_FZI_Mistral-7B_label-only_Greedy
checkpoint = outputs/models/trained-FZI_Mistral-7B_label-only/checkpoint-1185
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/FZI_Prompts.json
prompt_name = FZI_Mistral7B_label-only_prompt
batch_size = 1
sample = False
max_new_tokens = 100
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/trained_models/FZI/trained_FZI_Mistral-7B_label-only/
random_seed = 0
timestamp = 2024-10-21_12-50

---

