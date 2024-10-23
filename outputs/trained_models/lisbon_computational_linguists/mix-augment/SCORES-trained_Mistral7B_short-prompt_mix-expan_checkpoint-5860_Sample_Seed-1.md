# Full Evaluation Scores

File name: trained_Mistral7B_short-prompt_mix-expan_checkpoint-5860_Sample_Seed-1.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                70.9        34.3          52.0        52.4

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.709
Control_Precision: 0.980
Control_Recall: 0.556

## Overall Contrast Score

Contrast_F1: 0.542
Contrast_Precision: 0.950
Contrast_Recall: 0.379
**Official Metric ->** Faithfulness: 0.343
**Official Metric ->** Consistency: 0.520

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.704
Para_Precision: 0.976
Para_Recall: 0.550
Para_Consistency: 0.589


### Numerical Paraphrase

Numerical_Para_F1: 0.612
Numerical_Para_Precision: 0.901
Numerical_Para_Recall: 0.463
Numerical_Para_Consistency: 0.536


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.325
Cont_Consistency: 0.303


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.456
Numerical_Cont_Consistency: 0.444


## Text_Append Scores

Text_Append_F1: 0.681
Text_Append_Precision: 0.929
Text_Append_Recall: 0.538
Text_Append_Consistency: 0.565

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_Mistral7B_short-prompt_mix-expan_checkpoint-5860_Sample
checkpoint = outputs/models/baseline_Mistral-7B_training_long-prompt_mix-expand/checkpoint-5860
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/Baseline_Prompts.json
prompt_name = Mistral7B_short-prompt
batch_size = 16
sample = True
max_new_tokens = 8
temperature = 1.0
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/trained_models/lisbon_computational_linguists/mix-augment/
random_seed = 1
timestamp = 2024-10-22_21-39

---

