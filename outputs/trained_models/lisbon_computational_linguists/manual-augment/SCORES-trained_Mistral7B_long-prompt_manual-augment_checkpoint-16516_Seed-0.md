# Full Evaluation Scores

File name: trained_Mistral7B_long-prompt_manual-augment_checkpoint-16516_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                77.6        83.4          69.9        77.0

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.776
Control_Precision: 0.760
Control_Recall: 0.792

## Overall Contrast Score

Contrast_F1: 0.517
Contrast_Precision: 0.466
Contrast_Recall: 0.580
**Official Metric ->** Faithfulness: 0.834
**Official Metric ->** Consistency: 0.699

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.750
Para_Precision: 0.748
Para_Recall: 0.752
Para_Consistency: 0.751


### Numerical Paraphrase

Numerical_Para_F1: 0.617
Numerical_Para_Precision: 0.505
Numerical_Para_Recall: 0.793
Numerical_Para_Consistency: 0.746


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.827
Cont_Consistency: 0.784


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.886
Numerical_Cont_Consistency: 0.963


## Text_Append Scores

Text_Append_F1: 0.294
Text_Append_Precision: 0.179
Text_Append_Recall: 0.822
Text_Append_Consistency: 0.570

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_Mistral7B_long-prompt_manual-augment_checkpoint-16516
checkpoint = outputs/models/baseline_Mistral-7B_training_short-prompt_manual-augment/checkpoint-16516
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/Baseline_Prompts.json
prompt_name = Mistral7B_short-prompt
batch_size = 16
sample = False
max_new_tokens = 25
temperature = 1.0
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/trained_models/lisbon_computational_linguists/manual-augment/
random_seed = 0
timestamp = 2024-10-22_18-52

---

