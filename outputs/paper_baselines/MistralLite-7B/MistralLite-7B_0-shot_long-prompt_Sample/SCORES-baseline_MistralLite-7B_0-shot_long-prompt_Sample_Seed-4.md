# Full Evaluation Scores

File name: baseline_MistralLite-7B_0-shot_long-prompt_Sample_Seed-4.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                49.9        67.6          57.7        58.4

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.499
Control_Precision: 0.472
Control_Recall: 0.529

## Overall Contrast Score

Contrast_F1: 0.438
Contrast_Precision: 0.497
Contrast_Recall: 0.392
**Official Metric ->** Faithfulness: 0.676
**Official Metric ->** Consistency: 0.577

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.543
Para_Precision: 0.532
Para_Recall: 0.554
Para_Consistency: 0.552


### Numerical Paraphrase

Numerical_Para_F1: 0.454
Numerical_Para_Precision: 0.462
Numerical_Para_Recall: 0.447
Numerical_Para_Consistency: 0.549


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.675
Cont_Consistency: 0.672


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.684
Numerical_Cont_Consistency: 0.667


## Text_Append Scores

Text_Append_F1: 0.509
Text_Append_Precision: 0.467
Text_Append_Recall: 0.559
Text_Append_Consistency: 0.549

---

## Full Arg List

model = amazon/MistralLite
exp_name = baseline_MistralLite-7B_0-shot_long-prompt_Sample
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/Baseline_Prompts.json
prompt_name = MistralLite-7B_long-prompt
batch_size = 1
sample = True
max_new_tokens = 10
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/paper_baselines/MistralLite-7B/MistralLite-7B_0-shot_long-prompt_Sample/
random_seed = 4

---

