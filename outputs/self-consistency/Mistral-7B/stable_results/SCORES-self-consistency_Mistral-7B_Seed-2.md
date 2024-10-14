# Full Evaluation Scores

File name: self-consistency_Mistral-7B_Seed-2.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                72.5        73.8          65.8        70.7

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.725
Control_Precision: 0.768
Control_Recall: 0.686

## Overall Contrast Score

Contrast_F1: 0.521
Contrast_Precision: 0.561
Contrast_Recall: 0.486
**Official Metric ->** Faithfulness: 0.738
**Official Metric ->** Consistency: 0.658

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.695
Para_Precision: 0.744
Para_Recall: 0.652
Para_Consistency: 0.673


### Numerical Paraphrase

Numerical_Para_F1: 0.468
Numerical_Para_Precision: 0.396
Numerical_Para_Recall: 0.571
Numerical_Para_Consistency: 0.634


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.719
Cont_Consistency: 0.679


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.868
Numerical_Cont_Consistency: 0.883


## Text_Append Scores

Text_Append_F1: 0.506
Text_Append_Precision: 0.399
Text_Append_Recall: 0.692
Text_Append_Consistency: 0.611

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
random_seed = 2

---

