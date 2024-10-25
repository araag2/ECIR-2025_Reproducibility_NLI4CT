# Full Evaluation Scores

File name: trained_Mistral7B_short-prompt_mix-expand_checkpoint-232_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                70.9        38.2          53.1        54.1

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.709
Control_Precision: 0.972
Control_Recall: 0.559

## Overall Contrast Score

Contrast_F1: 0.545
Contrast_Precision: 0.933
Contrast_Recall: 0.385
**Official Metric ->** Faithfulness: 0.382
**Official Metric ->** Consistency: 0.531

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.705
Para_Precision: 0.971
Para_Recall: 0.553
Para_Consistency: 0.593


### Numerical Paraphrase

Numerical_Para_F1: 0.614
Numerical_Para_Precision: 0.890
Numerical_Para_Recall: 0.468
Numerical_Para_Consistency: 0.545


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.367
Cont_Consistency: 0.332


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.482
Numerical_Cont_Consistency: 0.494


## Text_Append Scores

Text_Append_F1: 0.677
Text_Append_Precision: 0.901
Text_Append_Recall: 0.542
Text_Append_Consistency: 0.569

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_Mistral7B_short-prompt_mix-expand_checkpoint-232
checkpoint = outputs/models/baseline_Mistral-7B_training_long-prompt_mix-expand/checkpoint-232
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/Baseline_Prompts.json
prompt_name = Mistral7B_short-prompt
batch_size = 16
sample = False
max_new_tokens = 8
temperature = 1.0
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/trained_models/lisbon_computational_linguists/mix-expand_checkpoint-232/
random_seed = 0
timestamp = 2024-10-25_13-32

---

