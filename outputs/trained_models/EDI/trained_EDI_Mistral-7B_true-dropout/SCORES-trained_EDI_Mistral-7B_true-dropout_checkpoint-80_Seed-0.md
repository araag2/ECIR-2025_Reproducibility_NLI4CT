# Full Evaluation Scores

File name: trained_EDI_Mistral-7B_true-dropout_checkpoint-80_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                79.6        74.3          69.8        74.6

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.796
Control_Precision: 0.860
Control_Recall: 0.741

## Overall Contrast Score

Contrast_F1: 0.544
Contrast_Precision: 0.552
Contrast_Recall: 0.536
**Official Metric ->** Faithfulness: 0.743
**Official Metric ->** Consistency: 0.698

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.756
Para_Precision: 0.797
Para_Recall: 0.720
Para_Consistency: 0.743


### Numerical Paraphrase

Numerical_Para_F1: 0.630
Numerical_Para_Precision: 0.560
Numerical_Para_Recall: 0.718
Numerical_Para_Consistency: 0.732


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.739
Cont_Consistency: 0.739


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.772
Numerical_Cont_Consistency: 0.895


## Text_Append Scores

Text_Append_F1: 0.437
Text_Append_Precision: 0.307
Text_Append_Recall: 0.759
Text_Append_Consistency: 0.605

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_EDI_Mistral-7B_true-dropout_checkpoint-80
checkpoint = outputs/models/trained-EDI_Mistral-7B_true-dropout/checkpoint-80
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/EDI_Prompts.json
prompt_name = EDI_Mistral7B_prompt
batch_size = 6
sample = False
max_new_tokens = 10
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/trained_models/EDI/trained_EDI_Mistral-7B_true-dropout/
random_seed = 0
timestamp = 2024-10-24_13-56

---

