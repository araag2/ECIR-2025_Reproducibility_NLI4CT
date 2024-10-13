# Full Evaluation Scores

File name: baseline_MistralLite-7B_0-shot_short-prompt_Sample_Seed-4.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                42.3        82.9          60.3        61.8

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.423
Control_Precision: 0.332
Control_Recall: 0.585

## Overall Contrast Score

Contrast_F1: 0.341
Contrast_Precision: 0.291
Contrast_Recall: 0.412
**Official Metric ->** Faithfulness: 0.829
**Official Metric ->** Consistency: 0.603

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.427
Para_Precision: 0.336
Para_Recall: 0.585
Para_Consistency: 0.549


### Numerical Paraphrase

Numerical_Para_F1: 0.382
Numerical_Para_Precision: 0.319
Numerical_Para_Recall: 0.475
Numerical_Para_Consistency: 0.580


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.840
Cont_Consistency: 0.821


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.754
Numerical_Cont_Consistency: 0.796


## Text_Append Scores

Text_Append_F1: 0.341
Text_Append_Precision: 0.243
Text_Append_Recall: 0.572
Text_Append_Consistency: 0.531

---

## Full Arg List

model = amazon/MistralLite
exp_name = baseline_MistralLite-7B_0-shot_short-prompt_Sample
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/Baseline_Prompts.json
prompt_name = MistralLite-7B_short-prompt
batch_size = 1
sample = True
max_new_tokens = 10
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/paper_baselines/MistralLite-7B/MistralLite-7B_0-shot_short-prompt_Sample/
random_seed = 4

---

