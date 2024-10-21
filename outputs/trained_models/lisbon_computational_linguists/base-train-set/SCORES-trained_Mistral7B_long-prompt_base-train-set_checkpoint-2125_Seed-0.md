# Full Evaluation Scores

File name: trained_Mistral7B_long-prompt_base-train-set_checkpoint-2125_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                78.0        72.3          69.1        73.1

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.780
Control_Precision: 0.800
Control_Recall: 0.760

## Overall Contrast Score

Contrast_F1: 0.544
Contrast_Precision: 0.569
Contrast_Recall: 0.521
**Official Metric ->** Faithfulness: 0.723
**Official Metric ->** Consistency: 0.691

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.754
Para_Precision: 0.799
Para_Recall: 0.714
Para_Consistency: 0.739


### Numerical Paraphrase

Numerical_Para_F1: 0.611
Numerical_Para_Precision: 0.560
Numerical_Para_Recall: 0.671
Numerical_Para_Consistency: 0.710


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.712
Cont_Consistency: 0.709


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.798
Numerical_Cont_Consistency: 0.901


## Text_Append Scores

Text_Append_F1: 0.465
Text_Append_Precision: 0.341
Text_Append_Recall: 0.731
Text_Append_Consistency: 0.608

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_Mistral7B_long-prompt_base-train-set_checkpoint-2125
checkpoint = outputs/models/baseline_Mistral-7B_training_short-prompt_Run-3/checkpoint-2125
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/Baseline_Prompts.json
prompt_name = Mistral7B_long-prompt
batch_size = 16
sample = False
max_new_tokens = 25
temperature = 1.0
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/trained_models/lisbon_computational_linguists/
random_seed = 0
timestamp = 2024-10-20_23-52

---

