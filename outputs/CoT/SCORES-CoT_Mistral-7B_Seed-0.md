# Full Evaluation Scores

File name: CoT_Mistral-7B_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                48.2        79.6          60.5        62.8

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.482
Control_Precision: 0.392
Control_Recall: 0.624

## Overall Contrast Score

Contrast_F1: 0.490
Contrast_Precision: 0.547
Contrast_Recall: 0.445
**Official Metric ->** Faithfulness: 0.796
**Official Metric ->** Consistency: 0.605

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.519
Para_Precision: 0.456
Para_Recall: 0.603
Para_Consistency: 0.578


### Numerical Paraphrase

Numerical_Para_F1: 0.392
Numerical_Para_Precision: 0.330
Numerical_Para_Recall: 0.484
Numerical_Para_Consistency: 0.585


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.795
Cont_Consistency: 0.725


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.807
Numerical_Cont_Consistency: 0.809


## Text_Append Scores

Text_Append_F1: 0.598
Text_Append_Precision: 0.664
Text_Append_Recall: 0.544
Text_Append_Consistency: 0.554

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = CoT_Mistral-7B
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/CoT_Prompts.json
prompt_name = Mistral7B_CoT-prompt
batch_size = 8
sample = False
max_new_tokens = 1000
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = CoT_inference
icl_source = 
output_dir = outputs/CoT/
random_seed = 0

---

