# Full Evaluation Scores

File name: CoT_Mistral-7B_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                57.4        82.9          62.3        67.5

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.574
Control_Precision: 0.496
Control_Recall: 0.681

## Overall Contrast Score

Contrast_F1: 0.432
Contrast_Precision: 0.408
Contrast_Recall: 0.458
**Official Metric ->** Faithfulness: 0.829
**Official Metric ->** Consistency: 0.623

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.557
Para_Precision: 0.504
Para_Recall: 0.622
Para_Consistency: 0.599


### Numerical Paraphrase

Numerical_Para_F1: 0.377
Numerical_Para_Precision: 0.319
Numerical_Para_Recall: 0.460
Numerical_Para_Consistency: 0.571


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.825
Cont_Consistency: 0.803


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.851
Numerical_Cont_Consistency: 0.772


## Text_Append Scores

Text_Append_F1: 0.417
Text_Append_Precision: 0.323
Text_Append_Recall: 0.587
Text_Append_Consistency: 0.548

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

