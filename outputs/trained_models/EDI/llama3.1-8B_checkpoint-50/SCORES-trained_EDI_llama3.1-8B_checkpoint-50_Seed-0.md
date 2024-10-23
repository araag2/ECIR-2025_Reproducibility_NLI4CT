# Full Evaluation Scores

File name: trained_EDI_llama3.1-8B_checkpoint-50_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                81.0        73.6          73.7        76.1

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.810
Control_Precision: 0.872
Control_Recall: 0.757

## Overall Contrast Score

Contrast_F1: 0.625
Contrast_Precision: 0.688
Contrast_Recall: 0.572
**Official Metric ->** Faithfulness: 0.736
**Official Metric ->** Consistency: 0.737

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.794
Para_Precision: 0.840
Para_Recall: 0.753
Para_Consistency: 0.782


### Numerical Paraphrase

Numerical_Para_F1: 0.717
Numerical_Para_Precision: 0.736
Numerical_Para_Recall: 0.698
Numerical_Para_Consistency: 0.763


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.747
Cont_Consistency: 0.719


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.667
Numerical_Cont_Consistency: 0.858


## Text_Append Scores

Text_Append_F1: 0.627
Text_Append_Precision: 0.529
Text_Append_Recall: 0.768
Text_Append_Consistency: 0.685

---

## Full Arg List

model = meta-llama/Llama-3.1-8B-Instruct
exp_name = trained_EDI_llama3.1-8B_checkpoint-50
checkpoint = outputs/models/trained-EDI_llama3.1-8B/checkpoint-50
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/EDI_Prompts.json
prompt_name = EDI_llama-prompt
batch_size = 4
sample = False
max_new_tokens = 50
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/trained_models/EDI/llama3.1-8B_checkpoint-50/
random_seed = 0
timestamp = 2024-10-22_18-06

---

