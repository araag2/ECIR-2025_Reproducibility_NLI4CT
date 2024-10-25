# Full Evaluation Scores

File name: trained_Mistral7B_short-prompt_mix-expand_3_checkpoint-4650_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                71.2        37.0          52.8        53.7

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.712
Control_Precision: 0.976
Control_Recall: 0.561

## Overall Contrast Score

Contrast_F1: 0.544
Contrast_Precision: 0.937
Contrast_Recall: 0.383
**Official Metric ->** Faithfulness: 0.370
**Official Metric ->** Consistency: 0.528

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.704
Para_Precision: 0.972
Para_Recall: 0.552
Para_Consistency: 0.592


### Numerical Paraphrase

Numerical_Para_F1: 0.614
Numerical_Para_Precision: 0.890
Numerical_Para_Recall: 0.468
Numerical_Para_Consistency: 0.545


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.353
Cont_Consistency: 0.327


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.482
Numerical_Cont_Consistency: 0.488


## Text_Append Scores

Text_Append_F1: 0.676
Text_Append_Precision: 0.908
Text_Append_Recall: 0.539
Text_Append_Consistency: 0.565

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_Mistral7B_short-prompt_mix-expand_3_checkpoint-4650
checkpoint = outputs/models/baseline_Mistral-7B_training_long-prompt_mix-expand_3/checkpoint-4650
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
output_dir = outputs/trained_models/lisbon_computational_linguists/mix-expand_3_checkpoint-4650/
random_seed = 0
timestamp = 2024-10-25_11-02

---

