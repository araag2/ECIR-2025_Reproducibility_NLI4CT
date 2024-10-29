# Full Evaluation Scores

File name: trained_EDI_Mistral-7B_true-dropout_checkpoint-76_Sample_Seed-1.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                77.4        84.8          71.0        77.7

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.774
Control_Precision: 0.752
Control_Recall: 0.797

## Overall Contrast Score

Contrast_F1: 0.526
Contrast_Precision: 0.464
Contrast_Recall: 0.606
**Official Metric ->** Faithfulness: 0.848
**Official Metric ->** Consistency: 0.710

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.730
Para_Precision: 0.696
Para_Recall: 0.768
Para_Consistency: 0.743


### Numerical Paraphrase

Numerical_Para_F1: 0.573
Numerical_Para_Precision: 0.451
Numerical_Para_Recall: 0.788
Numerical_Para_Consistency: 0.728


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.847
Cont_Consistency: 0.817


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.860
Numerical_Cont_Consistency: 0.988


## Text_Append Scores

Text_Append_F1: 0.363
Text_Append_Precision: 0.233
Text_Append_Recall: 0.814
Text_Append_Consistency: 0.590

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_EDI_Mistral-7B_true-dropout_checkpoint-76_Sample
checkpoint = outputs/models/trained-EDI_Mistral-7B_true-dropout/checkpoint-76
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/EDI_Prompts.json
prompt_name = EDI_Mistral7B_prompt
batch_size = 8
sample = True
max_new_tokens = 10
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/trained_models/EDI/trained_EDI_Mistral-7B_true-dropout/
random_seed = 1
timestamp = 2024-10-24_15-42

---

