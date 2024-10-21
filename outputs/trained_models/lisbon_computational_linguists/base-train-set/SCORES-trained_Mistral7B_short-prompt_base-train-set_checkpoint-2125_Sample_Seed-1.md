# Full Evaluation Scores

File name: trained_Mistral7B_short-prompt_base-train-set_checkpoint-2125_Sample_Seed-1.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                79.7        78.8          70.4        76.3

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.797
Control_Precision: 0.816
Control_Recall: 0.779

## Overall Contrast Score

Contrast_F1: 0.551
Contrast_Precision: 0.544
Contrast_Recall: 0.559
**Official Metric ->** Faithfulness: 0.788
**Official Metric ->** Consistency: 0.704

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.756
Para_Precision: 0.775
Para_Recall: 0.738
Para_Consistency: 0.750


### Numerical Paraphrase

Numerical_Para_F1: 0.556
Numerical_Para_Precision: 0.462
Numerical_Para_Recall: 0.700
Numerical_Para_Consistency: 0.701


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.783
Cont_Consistency: 0.741


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.825
Numerical_Cont_Consistency: 0.920


## Text_Append Scores

Text_Append_F1: 0.457
Text_Append_Precision: 0.324
Text_Append_Recall: 0.776
Text_Append_Consistency: 0.615

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_Mistral7B_short-prompt_base-train-set_checkpoint-2125_Sample
checkpoint = outputs/models/baseline_Mistral-7B_training_short-prompt_Run-3/checkpoint-2125
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
output_dir = outputs/trained_models/lisbon_computational_linguists/base-train-set/
random_seed = 1
timestamp = 2024-10-21_01-11

---

