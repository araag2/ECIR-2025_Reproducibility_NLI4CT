# Full Evaluation Scores

File name: baseline_Mistral-7B_0-shot_short-prompt_Greedy_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                72.4        70.9          65.2        69.5

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.724
Control_Precision: 0.772
Control_Recall: 0.682

## Overall Contrast Score

Contrast_F1: 0.527
Contrast_Precision: 0.592
Contrast_Recall: 0.475
**Official Metric ->** Faithfulness: 0.709
**Official Metric ->** Consistency: 0.652

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.699
Para_Precision: 0.763
Para_Recall: 0.645
Para_Consistency: 0.671


### Numerical Paraphrase

Numerical_Para_F1: 0.554
Numerical_Para_Precision: 0.505
Numerical_Para_Recall: 0.613
Numerical_Para_Consistency: 0.670


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.692
Cont_Consistency: 0.653


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.825
Numerical_Cont_Consistency: 0.870


## Text_Append Scores

Text_Append_F1: 0.522
Text_Append_Precision: 0.432
Text_Append_Recall: 0.660
Text_Append_Consistency: 0.605

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = baseline_Mistral-7B_0-shot_short-prompt_Greedy
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/Baseline_Prompts.json
prompt_name = Mistral7B_short-prompt
batch_size = 1
sample = False
max_new_tokens = 10
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/paper_baselines/Mistral-7B/Mistral-7B_0-shot_short-prompt_Greedy/
random_seed = 0

---

