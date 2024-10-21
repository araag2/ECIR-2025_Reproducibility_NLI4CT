# Full Evaluation Scores

File name: trained_Mistral7B_short-prompt_base-train-set_checkpoint-2125_Sample_Seed-5.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                79.6        78.6          70.3        76.2

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.796
Control_Precision: 0.820
Control_Recall: 0.774

## Overall Contrast Score

Contrast_F1: 0.550
Contrast_Precision: 0.543
Contrast_Recall: 0.557
**Official Metric ->** Faithfulness: 0.786
**Official Metric ->** Consistency: 0.703

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.755
Para_Precision: 0.775
Para_Recall: 0.736
Para_Consistency: 0.749


### Numerical Paraphrase

Numerical_Para_F1: 0.583
Numerical_Para_Precision: 0.484
Numerical_Para_Recall: 0.733
Numerical_Para_Consistency: 0.719


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.780
Cont_Consistency: 0.739


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.825
Numerical_Cont_Consistency: 0.926


## Text_Append Scores

Text_Append_F1: 0.451
Text_Append_Precision: 0.319
Text_Append_Recall: 0.773
Text_Append_Consistency: 0.613

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
random_seed = 5
timestamp = 2024-10-21_03-19

---

