# Full Evaluation Scores

File name: baseline_MistralLite-7B_0-shot_short-prompt_Sample_Seed-2.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                38.4        81.9          60.1        60.2

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.384
Control_Precision: 0.288
Control_Recall: 0.576

## Overall Contrast Score

Contrast_F1: 0.342
Contrast_Precision: 0.295
Contrast_Recall: 0.407
**Official Metric ->** Faithfulness: 0.819
**Official Metric ->** Consistency: 0.601

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.434
Para_Precision: 0.343
Para_Recall: 0.592
Para_Consistency: 0.553


### Numerical Paraphrase

Numerical_Para_F1: 0.421
Numerical_Para_Precision: 0.352
Numerical_Para_Recall: 0.525
Numerical_Para_Consistency: 0.607


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.821
Cont_Consistency: 0.799


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.807
Numerical_Cont_Consistency: 0.815


## Text_Append Scores

Text_Append_F1: 0.336
Text_Append_Precision: 0.240
Text_Append_Recall: 0.561
Text_Append_Consistency: 0.526

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
random_seed = 2

---

