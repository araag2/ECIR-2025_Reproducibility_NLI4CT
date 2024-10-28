# Full Evaluation Scores

File name: new_scores


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                79.6        85.0          78.9        81.2

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.796
Control_Precision: 0.820
Control_Recall: 0.774

## Overall Contrast Score

Contrast_F1: 0.715
Contrast_Precision: 0.789
Contrast_Recall: 0.653
**Official Metric ->** Faithfulness: 0.850
**Official Metric ->** Consistency: 0.789

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.796
Para_Precision: 0.815
Para_Recall: 0.777
Para_Consistency: 0.791


### Numerical Paraphrase

Numerical_Para_F1: 0.663
Numerical_Para_Precision: 0.659
Numerical_Para_Recall: 0.667
Numerical_Para_Consistency: 0.728


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.847
Cont_Consistency: 0.811


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.868
Numerical_Cont_Consistency: 0.895


## Text_Append Scores

Text_Append_F1: 0.776
Text_Append_Precision: 0.780
Text_Append_Recall: 0.772
Text_Append_Consistency: 0.775

---

## Full Arg List

model = gemini-1.5-flash-002
exp_name = baseline_Gemini-flash_0-shot_long-prompt_Greedy
project = stone-passage-376622
location = europe-southwest1
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
timestamp = 2024-10-28_18-06

---
