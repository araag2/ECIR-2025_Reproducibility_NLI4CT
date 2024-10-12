# Full Evaluation Scores

File name: baseline_MistralLite-7B_0-shot_short-prompt_Sample_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                34.2            82.4              60.4           59.0

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.388
Control_Precision: 0.288
Control_Recall: 0.595

## Overall Contrast Score

Contrast_F1: 0.342
Contrast_Precision: 0.293
Contrast_Recall: 0.412
**Official Metric ->** Faithfulness: 0.824
**Official Metric ->** Consistency: 0.604

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.427
Para_Precision: 0.335
Para_Recall: 0.589
Para_Consistency: 0.551


### Numerical Paraphrase

Numerical_Para_F1: 0.428
Numerical_Para_Precision: 0.374
Numerical_Para_Recall: 0.500
Numerical_Para_Consistency: 0.594


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.825
Cont_Consistency: 0.819


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.816
Numerical_Cont_Consistency: 0.840


## Text_Append Scores

Text_Append_F1: 0.337
Text_Append_Precision: 0.241
Text_Append_Recall: 0.560
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
random_seed = 0

---

