# Full Evaluation Scores

File name: baseline_MistralLite-7B_0-shot_long-prompt_Sample_Seed-3.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                54.3        61.6          54.6        56.8

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.543
Control_Precision: 0.528
Control_Recall: 0.559

## Overall Contrast Score

Contrast_F1: 0.394
Contrast_Precision: 0.451
Contrast_Recall: 0.349
**Official Metric ->** Faithfulness: 0.616
**Official Metric ->** Consistency: 0.546

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.489
Para_Precision: 0.465
Para_Recall: 0.516
Para_Consistency: 0.514


### Numerical Paraphrase

Numerical_Para_F1: 0.440
Numerical_Para_Precision: 0.462
Numerical_Para_Recall: 0.420
Numerical_Para_Consistency: 0.522


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.615
Cont_Consistency: 0.673


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.623
Numerical_Cont_Consistency: 0.586


## Text_Append Scores

Text_Append_F1: 0.472
Text_Append_Precision: 0.436
Text_Append_Recall: 0.515
Text_Append_Consistency: 0.513

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
random_seed = 3

---

