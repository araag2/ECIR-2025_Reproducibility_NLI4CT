# Full Evaluation Scores

File name: baseline_Mistral-7B_0-shot_long-prompt_Greedy_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                70.6        56.6          62.0        63.1

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.706
Control_Precision: 0.812
Control_Recall: 0.625

## Overall Contrast Score

Contrast_F1: 0.563
Contrast_Precision: 0.788
Contrast_Recall: 0.438
**Official Metric ->** Faithfulness: 0.566
**Official Metric ->** Consistency: 0.620

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.721
Para_Precision: 0.859
Para_Recall: 0.621
Para_Consistency: 0.667


### Numerical Paraphrase

Numerical_Para_F1: 0.560
Numerical_Para_Precision: 0.615
Numerical_Para_Recall: 0.514
Numerical_Para_Consistency: 0.607


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.548
Cont_Consistency: 0.520


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.684
Numerical_Cont_Consistency: 0.716


## Text_Append Scores

Text_Append_F1: 0.657
Text_Append_Precision: 0.739
Text_Append_Recall: 0.591
Text_Append_Consistency: 0.614

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = baseline_Mistral-7B_0-shot_long-prompt_Greedy
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/Baseline_Prompts.json
prompt_name = Mistral7B_long-prompt
batch_size = 1
sample = False
max_new_tokens = 10
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/paper_baselines/Mistral-7B/Mistral-7B_0-shot_long-prompt_Greedy/
random_seed = 0

---

