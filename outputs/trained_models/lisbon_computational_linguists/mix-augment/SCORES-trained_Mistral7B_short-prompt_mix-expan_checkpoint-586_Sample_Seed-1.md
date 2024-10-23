# Full Evaluation Scores

File name: trained_Mistral7B_short-prompt_mix-expan_checkpoint-586_Sample_Seed-1.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                71.1        38.5          53.4        54.3

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.711
Control_Precision: 0.972
Control_Recall: 0.560

## Overall Contrast Score

Contrast_F1: 0.547
Contrast_Precision: 0.932
Contrast_Recall: 0.387
**Official Metric ->** Faithfulness: 0.385
**Official Metric ->** Consistency: 0.534

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.704
Para_Precision: 0.967
Para_Recall: 0.553
Para_Consistency: 0.593


### Numerical Paraphrase

Numerical_Para_F1: 0.616
Numerical_Para_Precision: 0.890
Numerical_Para_Recall: 0.471
Numerical_Para_Consistency: 0.549


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.371
Cont_Consistency: 0.335


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.482
Numerical_Cont_Consistency: 0.506


## Text_Append Scores

Text_Append_F1: 0.679
Text_Append_Precision: 0.903
Text_Append_Recall: 0.545
Text_Append_Consistency: 0.574

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_Mistral7B_short-prompt_mix-expan_checkpoint-586_Sample
checkpoint = outputs/models/baseline_Mistral-7B_training_long-prompt_mix-expand/checkpoint-586
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
timestamp = 2024-10-22_22-16

---

