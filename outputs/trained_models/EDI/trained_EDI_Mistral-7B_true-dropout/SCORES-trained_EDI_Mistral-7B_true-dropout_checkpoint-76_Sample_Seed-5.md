# Full Evaluation Scores

File name: trained_EDI_Mistral-7B_true-dropout_checkpoint-76_Sample_Seed-5.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                77.5        85.0          70.7        77.7

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.775
Control_Precision: 0.752
Control_Recall: 0.800

## Overall Contrast Score

Contrast_F1: 0.525
Contrast_Precision: 0.466
Contrast_Recall: 0.602
**Official Metric ->** Faithfulness: 0.850
**Official Metric ->** Consistency: 0.707

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.728
Para_Precision: 0.696
Para_Recall: 0.763
Para_Consistency: 0.740


### Numerical Paraphrase

Numerical_Para_F1: 0.569
Numerical_Para_Precision: 0.451
Numerical_Para_Recall: 0.774
Numerical_Para_Consistency: 0.723


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.847
Cont_Consistency: 0.816


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.868
Numerical_Cont_Consistency: 0.981


## Text_Append Scores

Text_Append_F1: 0.367
Text_Append_Precision: 0.239
Text_Append_Recall: 0.796
Text_Append_Consistency: 0.589

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
random_seed = 5
timestamp = 2024-10-24_17-36

---

