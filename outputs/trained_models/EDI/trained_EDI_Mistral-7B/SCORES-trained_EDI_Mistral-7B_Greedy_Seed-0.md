# Full Evaluation Scores

File name: trained_EDI_Mistral-7B_Greedy_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                72.4        69.2          64.8        68.8

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.724
Control_Precision: 0.788
Control_Recall: 0.670

## Overall Contrast Score

Contrast_F1: 0.528
Contrast_Precision: 0.606
Contrast_Recall: 0.468
**Official Metric ->** Faithfulness: 0.692
**Official Metric ->** Consistency: 0.648

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.703
Para_Precision: 0.783
Para_Recall: 0.638
Para_Consistency: 0.669


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
Cont_Consistency: 0.641


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.816
Numerical_Cont_Consistency: 0.827


## Text_Append Scores

Text_Append_F1: 0.527
Text_Append_Precision: 0.439
Text_Append_Recall: 0.661
Text_Append_Consistency: 0.607

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_EDI_Mistral-7B_Greedy
checkpoint = outputs/models/trained-EDI_Mistral-7B/checkpoint-530
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/Baseline_Prompts.json
prompt_name = Mistral7B_short-prompt
batch_size = 1
sample = False
max_new_tokens = 100
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/trained_models/EDI/trained_EDI_Mistral-7B/
random_seed = 0
timestamp = 2024-10-19_18-29

---

