# Full Evaluation Scores

File name: new_scores


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                80.5        79.3          73.8        77.9

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.805
Control_Precision: 0.844
Control_Recall: 0.770

## Overall Contrast Score

Contrast_F1: 0.631
Contrast_Precision: 0.677
Contrast_Recall: 0.590
**Official Metric ->** Faithfulness: 0.793
**Official Metric ->** Consistency: 0.738

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.763
Para_Precision: 0.820
Para_Recall: 0.713
Para_Consistency: 0.745


### Numerical Paraphrase

Numerical_Para_F1: 0.678
Numerical_Para_Precision: 0.637
Numerical_Para_Recall: 0.725
Numerical_Para_Consistency: 0.754


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.791
Cont_Consistency: 0.755


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.807
Numerical_Cont_Consistency: 0.938


## Text_Append Scores

Text_Append_F1: 0.641
Text_Append_Precision: 0.539
Text_Append_Recall: 0.792
Text_Append_Consistency: 0.699

---

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_Mistral7B_short-prompt_mix-expand_checkpoint-3255
checkpoint = outputs/models/baseline_Mistral-7B_training_long-prompt_mix-expand/checkpoint-3255
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
output_dir = outputs/trained_models/lisbon_computational_linguists/mix-expand_checkpoint-3255/
random_seed = 0
timestamp = 2024-10-26_15-03

---

