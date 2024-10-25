# Full Evaluation Scores

File name: trained_Mistral7B_short-prompt_mix-expand_checkpoint-2320_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                71.4        34.8          52.1        52.8

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.714
Control_Precision: 0.984
Control_Recall: 0.560

## Overall Contrast Score

Contrast_F1: 0.542
Contrast_Precision: 0.947
Contrast_Recall: 0.380
**Official Metric ->** Faithfulness: 0.348
**Official Metric ->** Consistency: 0.521

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.703
Para_Precision: 0.973
Para_Recall: 0.551
Para_Consistency: 0.589


### Numerical Paraphrase

Numerical_Para_F1: 0.615
Numerical_Para_Precision: 0.912
Numerical_Para_Recall: 0.464
Numerical_Para_Consistency: 0.536


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.331
Cont_Consistency: 0.307


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.465
Numerical_Cont_Consistency: 0.469


## Text_Append Scores

Text_Append_F1: 0.680
Text_Append_Precision: 0.925
Text_Append_Recall: 0.537
Text_Append_Consistency: 0.564

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_Mistral7B_short-prompt_mix-expand_checkpoint-2320
checkpoint = outputs/models/baseline_Mistral-7B_training_long-prompt_mix-expand/checkpoint-2320
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
output_dir = outputs/trained_models/lisbon_computational_linguists/mix-expand_checkpoint-2320/
random_seed = 0
timestamp = 2024-10-25_12-47

---

