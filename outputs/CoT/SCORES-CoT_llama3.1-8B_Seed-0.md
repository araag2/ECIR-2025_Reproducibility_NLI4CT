# Full Evaluation Scores

File name: CoT_llama3.1-8B_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                64.5        88.2          68.3        73.7

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.645
Control_Precision: 0.568
Control_Recall: 0.747

## Overall Contrast Score

Contrast_F1: 0.510
Contrast_Precision: 0.463
Contrast_Recall: 0.569
**Official Metric ->** Faithfulness: 0.882
**Official Metric ->** Consistency: 0.683

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.622
Para_Precision: 0.545
Para_Recall: 0.724
Para_Consistency: 0.669


### Numerical Paraphrase

Numerical_Para_F1: 0.500
Numerical_Para_Precision: 0.407
Numerical_Para_Recall: 0.649
Numerical_Para_Consistency: 0.670


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.899
Cont_Consistency: 0.813


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.772
Numerical_Cont_Consistency: 0.901


## Text_Append Scores

Text_Append_F1: 0.499
Text_Append_Precision: 0.387
Text_Append_Recall: 0.702
Text_Append_Consistency: 0.611

---

## Full Arg List

model = meta-llama/Llama-3.1-8B-Instruct
exp_name = CoT_llama3.1-8B
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/CoT_Prompts.json
prompt_name = llama_CoT-prompt
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

