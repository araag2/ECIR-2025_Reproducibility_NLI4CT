# Full Evaluation Scores

File name: trained_Mistral7B_short-prompt_base-train-set_checkpoint-5505_Sample_Seed-2.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                77.5        85.2          71.0        77.9

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.775
Control_Precision: 0.736
Control_Recall: 0.818

## Overall Contrast Score

Contrast_F1: 0.535
Contrast_Precision: 0.480
Contrast_Recall: 0.604
**Official Metric ->** Faithfulness: 0.852
**Official Metric ->** Consistency: 0.710

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.741
Para_Precision: 0.721
Para_Recall: 0.762
Para_Consistency: 0.748


### Numerical Paraphrase

Numerical_Para_F1: 0.618
Numerical_Para_Precision: 0.516
Numerical_Para_Recall: 0.770
Numerical_Para_Consistency: 0.741


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.845
Cont_Consistency: 0.795


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.895
Numerical_Cont_Consistency: 0.957


## Text_Append Scores

Text_Append_F1: 0.369
Text_Append_Precision: 0.235
Text_Append_Recall: 0.859
Text_Append_Consistency: 0.598

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
random_seed = 2
timestamp = 2024-10-21_01-40

---

