# Full Evaluation Scores

File name: baseline_Mistral-7B_0-shot_long-prompt_Sample_Seed-4.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                69.7        57.4          62.0        63.0

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.697
Control_Precision: 0.804
Control_Recall: 0.615

## Overall Contrast Score

Contrast_F1: 0.563
Contrast_Precision: 0.786
Contrast_Recall: 0.439
**Official Metric ->** Faithfulness: 0.574
**Official Metric ->** Consistency: 0.620

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.722
Para_Precision: 0.857
Para_Recall: 0.624
Para_Consistency: 0.671


### Numerical Paraphrase

Numerical_Para_F1: 0.542
Numerical_Para_Precision: 0.604
Numerical_Para_Recall: 0.491
Numerical_Para_Consistency: 0.585


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.551
Cont_Consistency: 0.516


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.728
Numerical_Cont_Consistency: 0.722


## Text_Append Scores

Text_Append_F1: 0.657
Text_Append_Precision: 0.736
Text_Append_Recall: 0.593
Text_Append_Consistency: 0.615

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = baseline_Mistral-7B_0-shot_long-prompt_Sample
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/Baseline_Prompts.json
prompt_name = Mistral7B_long-prompt
batch_size = 1
sample = True
max_new_tokens = 10
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/paper_baselines/Mistral-7B/Mistral-7B_0-shot_long-prompt_Sample/
random_seed = 4

---
