# Full Evaluation Scores

File name: baseline_Gemini-pro_0-shot_long-prompt_Greedy_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                73.6        92.1          74.1        79.9

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.736
Control_Precision: 0.652
Control_Recall: 0.845

## Overall Contrast Score

Contrast_F1: 0.565
Contrast_Precision: 0.466
Contrast_Recall: 0.719
**Official Metric ->** Faithfulness: 0.921
**Official Metric ->** Consistency: 0.741

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.728
Para_Precision: 0.645
Para_Recall: 0.834
Para_Consistency: 0.759


### Numerical Paraphrase

Numerical_Para_F1: 0.511
Numerical_Para_Precision: 0.385
Numerical_Para_Recall: 0.761
Numerical_Para_Consistency: 0.701


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.920
Cont_Consistency: 0.888


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.930
Numerical_Cont_Consistency: 0.981


## Text_Append Scores

Text_Append_F1: 0.444
Text_Append_Precision: 0.296
Text_Append_Recall: 0.892
Text_Append_Consistency: 0.630

---

## Full Arg List

model = gemini-1.5-pro-001
exp_name = baseline_Gemini-pro_0-shot_long-prompt_Greedy
project = stone-passage-376622
location = europe-central2
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
prompt_file = src/prompts/Baseline_Prompts.json
prompt_name = Mistral7B_long-prompt
batch_size = 1
max_new_tokens = 10
temperature = 0.01
top_k = 40
top_p = 0.99
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/paper_baselines/Gemini/Gemini-pro_0-shot_long-prompt_Greedy/
random_seed = 0
sample = True
timestamp = 2024-10-29_01-43

---

