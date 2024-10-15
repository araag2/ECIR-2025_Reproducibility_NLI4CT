# Full Evaluation Scores

File name: icl_CoT-ver_1-shot_Mistral7B_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                57.4        74.0          62.1        64.5

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.574
Control_Precision: 0.552
Control_Recall: 0.597

## Overall Contrast Score

Contrast_F1: 0.514
Contrast_Precision: 0.596
Contrast_Recall: 0.452
**Official Metric ->** Faithfulness: 0.740
**Official Metric ->** Consistency: 0.621

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.595
Para_Precision: 0.579
Para_Recall: 0.612
Para_Consistency: 0.606


### Numerical Paraphrase

Numerical_Para_F1: 0.431
Numerical_Para_Precision: 0.363
Numerical_Para_Recall: 0.532
Numerical_Para_Consistency: 0.612


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.729
Cont_Consistency: 0.687


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.807
Numerical_Cont_Consistency: 0.821


## Text_Append Scores

Text_Append_F1: 0.606
Text_Append_Precision: 0.641
Text_Append_Recall: 0.575
Text_Append_Consistency: 0.583

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = icl_CoT-ver_1-shot_Mistral7B
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/ICL_Prompts.json
prompt_name = icl-1_EDI-CoT-ver_Mistral7B_prompt
batch_size = 1
sample = False
max_new_tokens = 1000
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = icl_inference_CoT-ver_1-shot
icl_source = data/SemEval-2024/icl/icl_CoT-ver/icl_CoT-ver_EDI_GPT-4_Mistral-7B.json
output_dir = outputs/icl_CoT-ver_1-shot/
random_seed = 0
timestamp = 2024-10-15_06-41

---

