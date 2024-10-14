# Full Evaluation Scores

File name: icl_inference_1-shot_Mistral7B_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                46.6        81.7          62.3        63.5

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.466
Control_Precision: 0.372
Control_Recall: 0.624

## Overall Contrast Score

Contrast_F1: 0.409
Contrast_Precision: 0.373
Contrast_Recall: 0.451
**Official Metric ->** Faithfulness: 0.817
**Official Metric ->** Consistency: 0.623

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.463
Para_Precision: 0.376
Para_Recall: 0.601
Para_Consistency: 0.563


### Numerical Paraphrase

Numerical_Para_F1: 0.427
Numerical_Para_Precision: 0.308
Numerical_Para_Recall: 0.700
Numerical_Para_Consistency: 0.665


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.807
Cont_Consistency: 0.801


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.886
Numerical_Cont_Consistency: 0.944


## Text_Append Scores

Text_Append_F1: 0.458
Text_Append_Precision: 0.379
Text_Append_Recall: 0.578
Text_Append_Consistency: 0.551

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = icl_inference_1-shot_Mistral7B
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/ICL_Prompts.json
prompt_name = icl-1_EDI-label-only-Mistral7B_prompt
batch_size = 4
sample = False
max_new_tokens = 10
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = icl_inference_1-shot
icl_source = data/SemEval-2024/icl/icl_label-only/icl_label-only_EDI.json
output_dir = outputs/icl_1-shot/
random_seed = 0

---

