# Full Evaluation Scores

File name: SCORES-trained_FZI_Mistral-7B_CoT-ver_Greedy_Seed-1


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                73.9        84.7          69.7        76.1

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.739
Control_Precision: 0.724
Control_Recall: 0.754

## Overall Contrast Score

Contrast_F1: 0.519
Contrast_Precision: 0.471
Contrast_Recall: 0.579
**Official Metric ->** Faithfulness: 0.847
**Official Metric ->** Consistency: 0.697

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.724
Para_Precision: 0.688
Para_Recall: 0.763
Para_Consistency: 0.737


### Numerical Paraphrase

Numerical_Para_F1: 0.486
Numerical_Para_Precision: 0.385
Numerical_Para_Recall: 0.660
Numerical_Para_Consistency: 0.670


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.840
Cont_Consistency: 0.780


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.895
Numerical_Cont_Consistency: 0.957


## Text_Append Scores

Text_Append_F1: 0.392
Text_Append_Precision: 0.264
Text_Append_Recall: 0.762
Text_Append_Consistency: 0.591

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_FZI_Mistral-7B_CoT-ver_Greedy
checkpoint = outputs/models/trained-FZI_Mistral-7B_CoT-ver/checkpoint-980
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/FZI_Prompts.json
prompt_name = FZI_Mistral7B_CoT-ver_prompt
batch_size = 64
sample = False
max_new_tokens = 500
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = CoT_inference
icl_source = 
output_dir = outputs/trained_models/FZI/trained_FZI_Mistral-7B_CoT-ver/
random_seed = 1
timestamp = 2024-10-23_20-49

---

