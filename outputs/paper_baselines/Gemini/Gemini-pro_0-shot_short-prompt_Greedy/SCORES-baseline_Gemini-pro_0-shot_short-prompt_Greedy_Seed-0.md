# Full Evaluation Scores

File name: new_scores


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                76.6        92.6          77.7        82.3

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.766
Control_Precision: 0.688
Control_Recall: 0.864

## Overall Contrast Score

Contrast_F1: 0.649
Contrast_Precision: 0.573
Contrast_Recall: 0.747
**Official Metric ->** Faithfulness: 0.926
**Official Metric ->** Consistency: 0.777

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.737
Para_Precision: 0.648
Para_Recall: 0.854
Para_Consistency: 0.769


### Numerical Paraphrase

Numerical_Para_F1: 0.567
Numerical_Para_Precision: 0.440
Numerical_Para_Recall: 0.800
Numerical_Para_Consistency: 0.728


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.920
Cont_Consistency: 0.873


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.965
Numerical_Cont_Consistency: 0.988


## Text_Append Scores

Text_Append_F1: 0.648
Text_Append_Precision: 0.515
Text_Append_Recall: 0.875
Text_Append_Consistency: 0.721

---

## Full Arg List

model = gemini-1.5-pro-001
exp_name = baseline_Gemini-pro_0-shot_short-prompt_Greedy
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
output_dir = outputs/paper_baselines/Gemini/Gemini-pro_0-shot_short-prompt_Greedy/
random_seed = 0
sample = True
timestamp = 2024-10-28_21-39

---


