# Full Evaluation Scores

File name: icl_inference_2-shot_Mistral7B_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                51.1        86.3          65.7        67.7

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.511
Control_Precision: 0.384
Control_Recall: 0.762

## Overall Contrast Score

Contrast_F1: 0.425
Contrast_Precision: 0.356
Contrast_Recall: 0.525
**Official Metric ->** Faithfulness: 0.863
**Official Metric ->** Consistency: 0.657

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.520
Para_Precision: 0.409
Para_Recall: 0.712
Para_Consistency: 0.622


### Numerical Paraphrase

Numerical_Para_F1: 0.370
Numerical_Para_Precision: 0.242
Numerical_Para_Recall: 0.786
Numerical_Para_Consistency: 0.665


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.849
Cont_Consistency: 0.812


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.956
Numerical_Cont_Consistency: 0.994


## Text_Append Scores

Text_Append_F1: 0.429
Text_Append_Precision: 0.317
Text_Append_Recall: 0.661
Text_Append_Consistency: 0.577

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = icl_inference_2-shot_Mistral7B
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/ICL_Prompts.json
prompt_name = icl-2_EDI-label-only-Mistral7B_prompt
batch_size = 4
sample = False
max_new_tokens = 100
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = icl_inference_2-shot
icl_source = data/SemEval-2024/icl/icl_label-only/icl_label-only_EDI_Mistral-7B.json
output_dir = outputs/icl_2-shot/
random_seed = 0
timestamp = 2024-10-17_08-24

---

