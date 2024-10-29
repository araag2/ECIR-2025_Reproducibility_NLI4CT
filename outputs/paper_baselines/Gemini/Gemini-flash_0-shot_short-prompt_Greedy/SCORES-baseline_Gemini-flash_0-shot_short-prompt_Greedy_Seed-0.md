# Full Evaluation Scores

File name: baseline_Gemini-flash_0-shot_short-prompt_Greedy_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                75.5        86.3          75.2        79.0

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.755
Control_Precision: 0.704
Control_Recall: 0.815

## Overall Contrast Score

Contrast_F1: 0.628
Contrast_Precision: 0.606
Contrast_Recall: 0.651
**Official Metric ->** Faithfulness: 0.863
**Official Metric ->** Consistency: 0.752

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.745
Para_Precision: 0.715
Para_Recall: 0.778
Para_Consistency: 0.755


### Numerical Paraphrase

Numerical_Para_F1: 0.581
Numerical_Para_Precision: 0.473
Numerical_Para_Recall: 0.754
Numerical_Para_Consistency: 0.723


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.861
Cont_Consistency: 0.824


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.877
Numerical_Cont_Consistency: 0.957


## Text_Append Scores

Text_Append_F1: 0.627
Text_Append_Precision: 0.513
Text_Append_Recall: 0.805
Text_Append_Consistency: 0.695

---

## Full Arg List

model = gemini-1.5-flash-001
exp_name = baseline_Gemini-flash_0-shot_short-prompt_Greedy
project = stone-passage-376622
location = europe-central2
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
prompt_file = src/prompts/Baseline_Prompts.json
prompt_name = Mistral7B_short-prompt
batch_size = 1
max_new_tokens = 10
temperature = 0.01
top_k = 40
top_p = 0.99
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/paper_baselines/Gemini/Gemini-flash_0-shot_short-prompt_Greedy/
random_seed = 0
sample = True
timestamp = 2024-10-29_13-33

---

