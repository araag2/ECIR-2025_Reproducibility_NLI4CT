# Full Evaluation Scores

File name: trained_EDI_llama3.1-8B_checkpoint-50_Sample_Seed-4.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                80.5        74.1          73.4        76.0

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.805
Control_Precision: 0.868
Control_Recall: 0.751

## Overall Contrast Score

Contrast_F1: 0.621
Contrast_Precision: 0.683
Contrast_Recall: 0.570
**Official Metric ->** Faithfulness: 0.741
**Official Metric ->** Consistency: 0.734

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.793
Para_Precision: 0.835
Para_Recall: 0.755
Para_Consistency: 0.782


### Numerical Paraphrase

Numerical_Para_F1: 0.684
Numerical_Para_Precision: 0.703
Numerical_Para_Recall: 0.667
Numerical_Para_Consistency: 0.737


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.751
Cont_Consistency: 0.709


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.675
Numerical_Cont_Consistency: 0.858


## Text_Append Scores

Text_Append_F1: 0.626
Text_Append_Precision: 0.529
Text_Append_Recall: 0.766
Text_Append_Consistency: 0.684

---

## Full Arg List

model = meta-llama/Llama-3.1-8B-Instruct
exp_name = trained_EDI_llama3.1-8B_checkpoint-50_Sample
checkpoint = outputs/models/trained-EDI_llama3.1-8B/checkpoint-50
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/EDI_Prompts.json
prompt_name = EDI_llama-prompt
batch_size = 8
sample = True
max_new_tokens = 2
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/trained_models/EDI/llama3.1-8B_checkpoint-50/
random_seed = 4
timestamp = 2024-10-22_19-27

---

