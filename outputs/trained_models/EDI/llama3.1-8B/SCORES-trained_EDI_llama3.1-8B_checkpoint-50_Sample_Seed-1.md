# Full Evaluation Scores

File name: trained_EDI_llama3.1-8B_checkpoint-50_Sample_Seed-1.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                81.2        72.5          73.6        75.8

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.812
Control_Precision: 0.872
Control_Recall: 0.760

## Overall Contrast Score

Contrast_F1: 0.622
Contrast_Precision: 0.687
Contrast_Recall: 0.568
**Official Metric ->** Faithfulness: 0.725
**Official Metric ->** Consistency: 0.736

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.794
Para_Precision: 0.840
Para_Recall: 0.754
Para_Consistency: 0.783


### Numerical Paraphrase

Numerical_Para_F1: 0.688
Numerical_Para_Precision: 0.703
Numerical_Para_Recall: 0.674
Numerical_Para_Consistency: 0.741


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.736
Cont_Consistency: 0.715


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.649
Numerical_Cont_Consistency: 0.870


## Text_Append Scores

Text_Append_F1: 0.628
Text_Append_Precision: 0.532
Text_Append_Recall: 0.767
Text_Append_Consistency: 0.685

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
random_seed = 1
timestamp = 2024-10-22_18-35

---

