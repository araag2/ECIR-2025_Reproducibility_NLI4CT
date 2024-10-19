# Full Evaluation Scores

File name: baseline_SOLAR-10.7B-shot_long-prompt_Greedy_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                66.0        58.1          58.7        60.9

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.660
Control_Precision: 0.760
Control_Recall: 0.583

## Overall Contrast Score

Contrast_F1: 0.487
Contrast_Precision: 0.617
Contrast_Recall: 0.402
**Official Metric ->** Faithfulness: 0.581
**Official Metric ->** Consistency: 0.587

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.664
Para_Precision: 0.763
Para_Recall: 0.588
Para_Consistency: 0.615


### Numerical Paraphrase

Numerical_Para_F1: 0.594
Numerical_Para_Precision: 0.780
Numerical_Para_Recall: 0.480
Numerical_Para_Consistency: 0.567


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.591
Cont_Consistency: 0.615


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.518
Numerical_Cont_Consistency: 0.586


## Text_Append Scores

Text_Append_F1: 0.500
Text_Append_Precision: 0.452
Text_Append_Recall: 0.559
Text_Append_Consistency: 0.548

---

## Full Arg List

model = upstage/SOLAR-10.7B-v1.0
exp_name = baseline_SOLAR-10.7B-shot_long-prompt_Greedy
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/Baseline_Prompts.json
prompt_name = SOLAR-10.7B_long-prompt
batch_size = 1
sample = False
max_new_tokens = 10
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/paper_baselines/SOLAR-10.7B/SOLAR-10.7B_0-shot_long-prompt_Greedy/
random_seed = 0
timestamp = 2024-10-16_23-29

---

