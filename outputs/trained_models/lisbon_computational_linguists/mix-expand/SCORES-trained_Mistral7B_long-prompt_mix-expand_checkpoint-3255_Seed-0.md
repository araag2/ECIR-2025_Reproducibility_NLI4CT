# Full Evaluation Scores

File name: trained_Mistral7B_long-prompt_mix-expand_checkpoint-3255_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                75.0        78.4          70.2        74.5

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.750
Control_Precision: 0.732
Control_Recall: 0.769

## Overall Contrast Score

Contrast_F1: 0.553
Contrast_Precision: 0.552
Contrast_Recall: 0.554
**Official Metric ->** Faithfulness: 0.784
**Official Metric ->** Consistency: 0.702

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.745
Para_Precision: 0.763
Para_Recall: 0.728
Para_Consistency: 0.739


### Numerical Paraphrase

Numerical_Para_F1: 0.610
Numerical_Para_Precision: 0.549
Numerical_Para_Recall: 0.685
Numerical_Para_Consistency: 0.714


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.784
Cont_Consistency: 0.761


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.781
Numerical_Cont_Consistency: 0.895


## Text_Append Scores

Text_Append_F1: 0.468
Text_Append_Precision: 0.341
Text_Append_Recall: 0.746
Text_Append_Consistency: 0.613

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_Mistral7B_long-prompt_mix-expand_checkpoint-3255
checkpoint = outputs/models/baseline_Mistral-7B_training_long-prompt_mix-expand/checkpoint-3255
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/Baseline_Prompts.json
prompt_name = Mistral7B_long-prompt
batch_size = 16
sample = False
max_new_tokens = 8
temperature = 1.0
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/trained_models/lisbon_computational_linguists/mix-expand_checkpoint-3255/
random_seed = 0
timestamp = 2024-10-26_19-21

---

