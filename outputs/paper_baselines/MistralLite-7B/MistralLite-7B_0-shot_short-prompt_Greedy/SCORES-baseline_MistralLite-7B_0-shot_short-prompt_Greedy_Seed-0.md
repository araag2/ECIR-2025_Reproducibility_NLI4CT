# Full Evaluation Scores

File name: baseline_MistralLite-7B_0-shot_short-prompt_Greedy_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                33.8        89.5          61.6        61.6

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.338
Control_Precision: 0.232
Control_Recall: 0.624

## Overall Contrast Score

Contrast_F1: 0.305
Contrast_Precision: 0.231
Contrast_Recall: 0.447
**Official Metric ->** Faithfulness: 0.895
**Official Metric ->** Consistency: 0.616

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.374
Para_Precision: 0.276
Para_Recall: 0.580
Para_Consistency: 0.538


### Numerical Paraphrase

Numerical_Para_F1: 0.436
Numerical_Para_Precision: 0.319
Numerical_Para_Recall: 0.690
Numerical_Para_Consistency: 0.665


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.892
Cont_Consistency: 0.867


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.912
Numerical_Cont_Consistency: 0.926


## Text_Append Scores

Text_Append_F1: 0.272
Text_Append_Precision: 0.176
Text_Append_Recall: 0.597
Text_Append_Consistency: 0.529

---

## Full Arg List

model = amazon/MistralLite
exp_name = baseline_MistralLite-7B_0-shot_short-prompt_Greedy
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/Baseline_Prompts.json
prompt_name = MistralLite-7B_short-prompt
batch_size = 1
sample = False
max_new_tokens = 10
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/paper_baselines/MistralLite-7B/MistralLite-7B_0-shot_short-prompt_Greedy/
random_seed = 0

---

