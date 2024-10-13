# Full Evaluation Scores

File name: baseline_MistralLite-7B_0-shot_long-prompt_Greedy_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                58.0        68.4          59.4        61.9

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.580
Control_Precision: 0.572
Control_Recall: 0.588

## Overall Contrast Score

Contrast_F1: 0.438
Contrast_Precision: 0.478
Contrast_Recall: 0.404
**Official Metric ->** Faithfulness: 0.684
**Official Metric ->** Consistency: 0.594

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.544
Para_Precision: 0.527
Para_Recall: 0.563
Para_Consistency: 0.559


### Numerical Paraphrase

Numerical_Para_F1: 0.497
Numerical_Para_Precision: 0.484
Numerical_Para_Recall: 0.512
Numerical_Para_Consistency: 0.603


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.688
Cont_Consistency: 0.707


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.658
Numerical_Cont_Consistency: 0.685


## Text_Append Scores

Text_Append_F1: 0.493
Text_Append_Precision: 0.428
Text_Append_Recall: 0.583
Text_Append_Consistency: 0.561

---

## Full Arg List

model = amazon/MistralLite
exp_name = baseline_MistralLite-7B_0-shot_long-prompt_Greedy
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/Baseline_Prompts.json
prompt_name = MistralLite-7B_long-prompt
batch_size = 1
sample = False
max_new_tokens = 10
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/paper_baselines/MistralLite-7B/MistralLite-7B_0-shot_long-prompt_Greedy/
random_seed = 0

---

