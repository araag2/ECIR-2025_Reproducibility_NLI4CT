# Full Evaluation Scores

File name: baseline_Gemini-flash_0-shot_long-prompt_Greedy_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                71.6        84.7          71.8        76.0

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.716
Control_Precision: 0.660
Control_Recall: 0.782

## Overall Contrast Score

Contrast_F1: 0.554
Contrast_Precision: 0.507
Contrast_Recall: 0.610
**Official Metric ->** Faithfulness: 0.847
**Official Metric ->** Consistency: 0.718

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.718
Para_Precision: 0.681
Para_Recall: 0.759
Para_Consistency: 0.733


### Numerical Paraphrase

Numerical_Para_F1: 0.544
Numerical_Para_Precision: 0.473
Numerical_Para_Recall: 0.642
Numerical_Para_Consistency: 0.679


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.839
Cont_Consistency: 0.829


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.904
Numerical_Cont_Consistency: 0.932


## Text_Append Scores

Text_Append_F1: 0.477
Text_Append_Precision: 0.337
Text_Append_Recall: 0.814
Text_Append_Consistency: 0.630

---

## Full Arg List

model = gemini-1.5-flash-001
exp_name = baseline_Gemini-flash_0-shot_long-prompt_Greedy
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
output_dir = outputs/paper_baselines/Gemini/Gemini-flash_0-shot_long-prompt_Greedy/
random_seed = 0
sample = True
timestamp = 2024-10-29_14-08

---

