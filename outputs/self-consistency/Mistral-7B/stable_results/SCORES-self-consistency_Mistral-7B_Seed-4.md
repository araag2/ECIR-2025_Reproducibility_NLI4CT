# Full Evaluation Scores

File name: self-consistency_Mistral-7B_Seed-4.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                72.0        74.2          66.1        70.7

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.720
Control_Precision: 0.760
Control_Recall: 0.683

## Overall Contrast Score

Contrast_F1: 0.525
Contrast_Precision: 0.565
Contrast_Recall: 0.490
**Official Metric ->** Faithfulness: 0.742
**Official Metric ->** Consistency: 0.661

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.696
Para_Precision: 0.743
Para_Recall: 0.655
Para_Consistency: 0.675


### Numerical Paraphrase

Numerical_Para_F1: 0.477
Numerical_Para_Precision: 0.407
Numerical_Para_Recall: 0.578
Numerical_Para_Consistency: 0.638


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.724
Cont_Consistency: 0.679


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.860
Numerical_Cont_Consistency: 0.889


## Text_Append Scores

Text_Append_F1: 0.514
Text_Append_Precision: 0.407
Text_Append_Recall: 0.698
Text_Append_Consistency: 0.615

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
random_seed = 4

---

