# Full Evaluation Scores

File name: baseline_MistralLite-7B_0-shot_short-prompt_Sample_Seed-3.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                39.0        83.3          59.9        60.8

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.390
Control_Precision: 0.292
Control_Recall: 0.589

## Overall Contrast Score

Contrast_F1: 0.334
Contrast_Precision: 0.285
Contrast_Recall: 0.405
**Official Metric ->** Faithfulness: 0.833
**Official Metric ->** Consistency: 0.599

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.426
Para_Precision: 0.337
Para_Recall: 0.578
Para_Consistency: 0.545


### Numerical Paraphrase

Numerical_Para_F1: 0.397
Numerical_Para_Precision: 0.341
Numerical_Para_Recall: 0.477
Numerical_Para_Consistency: 0.580


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.836
Cont_Consistency: 0.823


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.816
Numerical_Cont_Consistency: 0.790


## Text_Append Scores

Text_Append_F1: 0.321
Text_Append_Precision: 0.225
Text_Append_Recall: 0.556
Text_Append_Consistency: 0.523

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
random_seed = 3

---

