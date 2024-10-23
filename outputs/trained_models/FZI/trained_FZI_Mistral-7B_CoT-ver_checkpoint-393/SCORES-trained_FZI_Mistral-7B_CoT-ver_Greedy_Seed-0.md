# Full Evaluation Scores

File name: trained_FZI_Mistral-7B_CoT-ver_Greedy_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                69.7        52.8          57.3        59.9

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.697
Control_Precision: 0.836
Control_Recall: 0.597

## Overall Contrast Score

Contrast_F1: 0.505
Contrast_Precision: 0.697
Contrast_Recall: 0.396
**Official Metric ->** Faithfulness: 0.528
**Official Metric ->** Consistency: 0.573

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.684
Para_Precision: 0.827
Para_Recall: 0.583
Para_Consistency: 0.618


### Numerical Paraphrase

Numerical_Para_F1: 0.592
Numerical_Para_Precision: 0.813
Numerical_Para_Recall: 0.465
Numerical_Para_Consistency: 0.545


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.535
Cont_Consistency: 0.515


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.482
Numerical_Cont_Consistency: 0.481


## Text_Append Scores

Text_Append_F1: 0.563
Text_Append_Precision: 0.553
Text_Append_Recall: 0.573
Text_Append_Consistency: 0.571

---

## Full Arg List

model = mistralai/Mistral-7B-Instruct-v0.2
exp_name = trained_FZI_Mistral-7B_CoT-ver_Greedy
checkpoint = outputs/models/trained-FZI_Mistral-7B_CoT-ver/checkpoint-393
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/FZI_Prompts.json
prompt_name = FZI_Mistral7B_CoT-ver_prompt
batch_size = 32
sample = False
max_new_tokens = 150
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = CoT_inference
icl_source = 
output_dir = outputs/trained_models/FZI/trained_FZI_Mistral-7B_CoT-ver_checkpoint-393/
random_seed = 0
timestamp = 2024-10-24_00-05

---

