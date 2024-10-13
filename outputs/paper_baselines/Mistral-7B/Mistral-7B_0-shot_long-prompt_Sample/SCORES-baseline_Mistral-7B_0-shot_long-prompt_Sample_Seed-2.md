# Full Evaluation Scores

File name: baseline_Mistral-7B_0-shot_long-prompt_Sample_Seed-2.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                70.1        56.5          61.8        62.8

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.701
Control_Precision: 0.808
Control_Recall: 0.620

## Overall Contrast Score

Contrast_F1: 0.560
Contrast_Precision: 0.781
Contrast_Recall: 0.436
**Official Metric ->** Faithfulness: 0.565
**Official Metric ->** Consistency: 0.618

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.720
Para_Precision: 0.857
Para_Recall: 0.620
Para_Consistency: 0.666


### Numerical Paraphrase

Numerical_Para_F1: 0.566
Numerical_Para_Precision: 0.637
Numerical_Para_Recall: 0.509
Numerical_Para_Consistency: 0.603


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.544
Cont_Consistency: 0.524


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.702
Numerical_Cont_Consistency: 0.716


## Text_Append Scores

Text_Append_F1: 0.649
Text_Append_Precision: 0.723
Text_Append_Recall: 0.588
Text_Append_Consistency: 0.609

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = baseline_Mistral-7B_0-shot_long-prompt_Sample
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/Baseline_Prompts.json
prompt_name = Mistral7B_long-prompt
batch_size = 1
sample = True
max_new_tokens = 10
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/paper_baselines/Mistral-7B/Mistral-7B_0-shot_long-prompt_Sample/
random_seed = 2

---

