# Full Evaluation Scores

File name: icl_inference_1-shot_llama3.1-8B_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                69.0        80.9          69.1        73.0

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.690
Control_Precision: 0.660
Control_Recall: 0.724

## Overall Contrast Score

Contrast_F1: 0.578
Contrast_Precision: 0.621
Contrast_Recall: 0.540
**Official Metric ->** Faithfulness: 0.809
**Official Metric ->** Consistency: 0.691

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.685
Para_Precision: 0.659
Para_Recall: 0.713
Para_Consistency: 0.697


### Numerical Paraphrase

Numerical_Para_F1: 0.503
Numerical_Para_Precision: 0.451
Numerical_Para_Recall: 0.569
Numerical_Para_Consistency: 0.638


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.801
Cont_Consistency: 0.756


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.860
Numerical_Cont_Consistency: 0.858


## Text_Append Scores

Text_Append_F1: 0.628
Text_Append_Precision: 0.604
Text_Append_Recall: 0.654
Text_Append_Consistency: 0.642

---

## Full Arg List

model = meta-llama/Llama-3.1-8B-Instruct
exp_name = icl_inference_1-shot_llama3.1-8B
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/ICL_Prompts.json
prompt_name = icl-1_EDI-label-only-llama3.1-8B_prompt
batch_size = 4
sample = False
max_new_tokens = 50
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = icl_inference_1-shot
icl_source = data/SemEval-2024/icl/icl_label-only/icl_label-only_EDI_llama3.1-8B.json
output_dir = outputs/icl_1-shot/
random_seed = 0
timestamp = 2024-10-16_21-50

---

