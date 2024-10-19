# Full Evaluation Scores

File name: icl_inference_2-shot_llama3.1-8B_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                70.2        74.3          68.1        70.9

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.702
Control_Precision: 0.732
Control_Recall: 0.675

## Overall Contrast Score

Contrast_F1: 0.594
Contrast_Precision: 0.709
Contrast_Recall: 0.512
**Official Metric ->** Faithfulness: 0.743
**Official Metric ->** Consistency: 0.681

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.705
Para_Precision: 0.725
Para_Recall: 0.686
Para_Consistency: 0.697


### Numerical Paraphrase

Numerical_Para_F1: 0.581
Numerical_Para_Precision: 0.593
Numerical_Para_Recall: 0.568
Numerical_Para_Consistency: 0.652


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.737
Cont_Consistency: 0.708


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.781
Numerical_Cont_Consistency: 0.827


## Text_Append Scores

Text_Append_F1: 0.663
Text_Append_Precision: 0.707
Text_Append_Recall: 0.625
Text_Append_Consistency: 0.641

---

## Full Arg List

model = meta-llama/Llama-3.1-8B-Instruct
exp_name = icl_inference_2-shot_llama3.1-8B
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/ICL_Prompts.json
prompt_name = icl-2_EDI-label-only-llama3.1-8B_prompt
batch_size = 4
sample = False
max_new_tokens = 50
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = icl_inference_2-shot
icl_source = data/SemEval-2024/icl/icl_label-only/icl_label-only_EDI_llama3.1-8B.json
output_dir = outputs/icl_2-shot/
random_seed = 0
timestamp = 2024-10-16_22-48

---

