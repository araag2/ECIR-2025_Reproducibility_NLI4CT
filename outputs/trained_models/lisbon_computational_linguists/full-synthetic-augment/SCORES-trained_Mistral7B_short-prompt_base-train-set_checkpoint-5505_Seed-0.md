# Full Evaluation Scores

File name: trained_Mistral7B_short-prompt_base-train-set_checkpoint-5505_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                77.5        85.4          70.7        77.9

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.775
Control_Precision: 0.736
Control_Recall: 0.818

## Overall Contrast Score

Contrast_F1: 0.528
Contrast_Precision: 0.471
Contrast_Recall: 0.601
**Official Metric ->** Faithfulness: 0.854
**Official Metric ->** Consistency: 0.707

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.738
Para_Precision: 0.716
Para_Recall: 0.762
Para_Consistency: 0.746


### Numerical Paraphrase

Numerical_Para_F1: 0.609
Numerical_Para_Precision: 0.505
Numerical_Para_Recall: 0.767
Numerical_Para_Consistency: 0.737


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.848
Cont_Consistency: 0.789


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.895
Numerical_Cont_Consistency: 0.969


## Text_Append Scores

Text_Append_F1: 0.354
Text_Append_Precision: 0.223
Text_Append_Recall: 0.861
Text_Append_Consistency: 0.593

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_Mistral7B_short-prompt_base-train-set_checkpoint-5505
checkpoint = outputs/models/baseline_Mistral-7B_training_short-prompt_full-synthetic-expand/checkpoint-5505
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
output_dir = outputs/trained_models/lisbon_computational_linguists/full-synthetic-augment/
random_seed = 0
timestamp = 2024-10-21_00-59

---

