# Full Evaluation Scores

File name: trained_Mistral7B_short-prompt_base-train-set_checkpoint-5505_Sample_Seed-4.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                77.2        85.3          70.7        77.8

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.772
Control_Precision: 0.732
Control_Recall: 0.817

## Overall Contrast Score

Contrast_F1: 0.533
Contrast_Precision: 0.480
Contrast_Recall: 0.600
**Official Metric ->** Faithfulness: 0.853
**Official Metric ->** Consistency: 0.707

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.742
Para_Precision: 0.727
Para_Recall: 0.758
Para_Consistency: 0.747


### Numerical Paraphrase

Numerical_Para_F1: 0.627
Numerical_Para_Precision: 0.527
Numerical_Para_Recall: 0.774
Numerical_Para_Consistency: 0.746


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.848
Cont_Consistency: 0.787


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.886
Numerical_Cont_Consistency: 0.975


## Text_Append Scores

Text_Append_F1: 0.358
Text_Append_Precision: 0.227
Text_Append_Recall: 0.850
Text_Append_Consistency: 0.593

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_Mistral7B_short-prompt_base-train-set_checkpoint-5505_Sample
checkpoint = outputs/models/baseline_Mistral-7B_training_short-prompt_full-synthetic-expand/checkpoint-5505
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
output_dir = outputs/trained_models/lisbon_computational_linguists/full-synthetic-augment/
random_seed = 4
timestamp = 2024-10-21_02-14

---

