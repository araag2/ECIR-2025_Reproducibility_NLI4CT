# Full Evaluation Scores

File name: trained_Mistral-7B_short-prompt_manual-augment_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                72.2        69.2          64.8        68.7

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.722
Control_Precision: 0.788
Control_Recall: 0.666

## Overall Contrast Score

Contrast_F1: 0.529
Contrast_Precision: 0.607
Contrast_Recall: 0.468
**Official Metric ->** Faithfulness: 0.692
**Official Metric ->** Consistency: 0.648

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.703
Para_Precision: 0.781
Para_Recall: 0.640
Para_Consistency: 0.671


### Numerical Paraphrase

Numerical_Para_F1: 0.571
Numerical_Para_Precision: 0.527
Numerical_Para_Recall: 0.623
Numerical_Para_Consistency: 0.679


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.673
Cont_Consistency: 0.637


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.816
Numerical_Cont_Consistency: 0.833


## Text_Append Scores

Text_Append_F1: 0.530
Text_Append_Precision: 0.443
Text_Append_Recall: 0.659
Text_Append_Consistency: 0.607

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_Mistral-7B_short-prompt_manual-augment
checkpoint = outputs/models/baseline_Mistral-7B_training_short-prompt_manual-augment/checkpoint-586
merge = True
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
output_dir = outputs/trained_models/lisbon_computational_linguists/
random_seed = 0
timestamp = 2024-10-17_16-13

---

