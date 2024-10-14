# Full Evaluation Scores

File name: self-consistency_Mistral-7B_Seed-3.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                72.1        73.6          65.8        70.5

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.721
Control_Precision: 0.764
Control_Recall: 0.682

## Overall Contrast Score

Contrast_F1: 0.522
Contrast_Precision: 0.564
Contrast_Recall: 0.486
**Official Metric ->** Faithfulness: 0.736
**Official Metric ->** Consistency: 0.658

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.696
Para_Precision: 0.744
Para_Recall: 0.653
Para_Consistency: 0.675


### Numerical Paraphrase

Numerical_Para_F1: 0.474
Numerical_Para_Precision: 0.407
Numerical_Para_Recall: 0.569
Numerical_Para_Consistency: 0.634


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.719
Cont_Consistency: 0.677


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.851
Numerical_Cont_Consistency: 0.883


## Text_Append Scores

Text_Append_F1: 0.509
Text_Append_Precision: 0.403
Text_Append_Recall: 0.693
Text_Append_Consistency: 0.612

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = self-consistency_Mistral-7B
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/self-consistency_prompts.json
prompt_name = Mistral7B
batch_size = 1
sample = True
max_new_tokens = 10
temperature = 0.7
top_k = 50
top_p = 0.99
num_return_sequences = 10
task_type = self-consistency_inference
icl_source = 
output_dir = outputs/self-consistency/Mistral-7B/
random_seed = 3

---

