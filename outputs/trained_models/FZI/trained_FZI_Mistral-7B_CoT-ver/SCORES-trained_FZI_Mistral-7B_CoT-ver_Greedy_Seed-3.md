# Full Evaluation Scores

File name: trained_FZI_Mistral-7B_CoT-ver_Greedy_Seed-3.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                61.6        83.2          65.1        70.0

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.616
Control_Precision: 0.552
Control_Recall: 0.697

## Overall Contrast Score

Contrast_F1: 0.441
Contrast_Precision: 0.393
Contrast_Recall: 0.502
**Official Metric ->** Faithfulness: 0.832
**Official Metric ->** Consistency: 0.651

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.571
Para_Precision: 0.477
Para_Recall: 0.712
Para_Consistency: 0.642


### Numerical Paraphrase

Numerical_Para_F1: 0.431
Numerical_Para_Precision: 0.341
Numerical_Para_Recall: 0.585
Numerical_Para_Consistency: 0.634


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.821
Cont_Consistency: 0.788


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.904
Numerical_Cont_Consistency: 0.914


## Text_Append Scores

Text_Append_F1: 0.422
Text_Append_Precision: 0.316
Text_Append_Recall: 0.634
Text_Append_Consistency: 0.567

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_FZI_Mistral-7B_CoT-ver_Greedy
checkpoint = outputs/models/trained-FZI_Mistral-7B_CoT-ver/checkpoint-980
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/FZI_Prompts.json
prompt_name = FZI_Mistral7B_CoT-ver_prompt
batch_size = 64
sample = False
max_new_tokens = 500
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = CoT_inference
icl_source = 
output_dir = outputs/trained_models/FZI/trained_FZI_Mistral-7B_CoT-ver/
random_seed = 3
timestamp = 2024-10-24_10-53

---

