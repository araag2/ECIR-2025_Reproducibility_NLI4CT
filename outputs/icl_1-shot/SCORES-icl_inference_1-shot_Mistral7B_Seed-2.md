# Full Evaluation Scores

File name: icl_inference_1-shot_Mistral7B_Seed-2.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                48.8        88.3          65.2        67.4

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.488
Control_Precision: 0.364
Control_Recall: 0.740

## Overall Contrast Score

Contrast_F1: 0.405
Contrast_Precision: 0.330
Contrast_Recall: 0.526
**Official Metric ->** Faithfulness: 0.883
**Official Metric ->** Consistency: 0.652

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.502
Para_Precision: 0.393
Para_Recall: 0.692
Para_Consistency: 0.609


### Numerical Paraphrase

Numerical_Para_F1: 0.356
Numerical_Para_Precision: 0.231
Numerical_Para_Recall: 0.778
Numerical_Para_Consistency: 0.661


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.869
Cont_Consistency: 0.844


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.974
Numerical_Cont_Consistency: 0.994


## Text_Append Scores

Text_Append_F1: 0.388
Text_Append_Precision: 0.279
Text_Append_Recall: 0.639
Text_Append_Consistency: 0.561

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
random_seed = 2

---

