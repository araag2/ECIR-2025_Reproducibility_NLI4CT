# Full Evaluation Scores

File name: baseline_Mistral-7B_0-shot_long-prompt_Sample_Seed-3.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                70.6        56.7          61.7        63.0

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.706
Control_Precision: 0.820
Control_Recall: 0.619

## Overall Contrast Score

Contrast_F1: 0.560
Contrast_Precision: 0.785
Contrast_Recall: 0.436
**Official Metric ->** Faithfulness: 0.567
**Official Metric ->** Consistency: 0.617

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.717
Para_Precision: 0.853
Para_Recall: 0.619
Para_Consistency: 0.664


### Numerical Paraphrase

Numerical_Para_F1: 0.563
Numerical_Para_Precision: 0.637
Numerical_Para_Recall: 0.504
Numerical_Para_Consistency: 0.598


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.545
Cont_Consistency: 0.517


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.711
Numerical_Cont_Consistency: 0.698


## Text_Append Scores

Text_Append_F1: 0.655
Text_Append_Precision: 0.735
Text_Append_Recall: 0.591
Text_Append_Consistency: 0.613

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
random_seed = 3

---

