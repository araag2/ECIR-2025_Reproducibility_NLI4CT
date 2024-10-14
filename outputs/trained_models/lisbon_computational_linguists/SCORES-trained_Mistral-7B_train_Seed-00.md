# Full Evaluation Scores

File name: trained_Mistral-7B_train_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                69.8        57.1          62.0        63.0

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.698
Control_Precision: 0.800
Control_Recall: 0.619

## Overall Contrast Score

Contrast_F1: 0.560
Contrast_Precision: 0.777
Contrast_Recall: 0.438
**Official Metric ->** Faithfulness: 0.571
**Official Metric ->** Consistency: 0.620

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.717
Para_Precision: 0.852
Para_Recall: 0.619
Para_Consistency: 0.664


### Numerical Paraphrase

Numerical_Para_F1: 0.571
Numerical_Para_Precision: 0.615
Numerical_Para_Recall: 0.533
Numerical_Para_Consistency: 0.625


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.551
Cont_Consistency: 0.521


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.702
Numerical_Cont_Consistency: 0.722


## Text_Append Scores

Text_Append_F1: 0.651
Text_Append_Precision: 0.723
Text_Append_Recall: 0.593
Text_Append_Consistency: 0.613

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_Mistral-7B_train
checkpoint = outputs/models/checkpoint-850
merge = True
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/Baseline_Prompts.json
prompt_name = Mistral7B_long-prompt
batch_size = 16
sample = False
max_new_tokens = 10
temperature = 1.0
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/trained_models/lisbon_computational_linguists/
random_seed = 0

---

