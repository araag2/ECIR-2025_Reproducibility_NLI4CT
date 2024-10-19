# Full Evaluation Scores

File name: baseline_SOLAR-10.7B-shot_short-prompt_Greedy_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                66.9        15.3          43.9        42.0

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.669
Control_Precision: 0.968
Control_Recall: 0.511

## Overall Contrast Score

Contrast_F1: 0.501
Contrast_Precision: 0.963
Contrast_Recall: 0.339
**Official Metric ->** Faithfulness: 0.153
**Official Metric ->** Consistency: 0.439

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.673
Para_Precision: 0.971
Para_Recall: 0.514
Para_Consistency: 0.527


### Numerical Paraphrase

Numerical_Para_F1: 0.579
Numerical_Para_Precision: 0.967
Numerical_Para_Recall: 0.413
Numerical_Para_Consistency: 0.429


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.159
Cont_Consistency: 0.183


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.114
Numerical_Cont_Consistency: 0.136


## Text_Append Scores

Text_Append_F1: 0.663
Text_Append_Precision: 0.955
Text_Append_Recall: 0.507
Text_Append_Consistency: 0.514

---

## Full Arg List

model = upstage/SOLAR-10.7B-v1.0
exp_name = baseline_SOLAR-10.7B-shot_short-prompt_Greedy
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/Baseline_Prompts.json
prompt_name = SOLAR-10.7B_short-prompt
batch_size = 1
sample = False
max_new_tokens = 10
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/paper_baselines/SOLAR-10.7B/SOLAR-10.7B_0-shot_short-prompt_Greedy/
random_seed = 0
timestamp = 2024-10-16_03-38

---

