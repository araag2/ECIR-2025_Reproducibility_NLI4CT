# Full Evaluation Scores

File name: baseline_BioMistral-7B_0-shot_long-prompt_Greedy_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                2.4        99.7          61.6        54.5

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.024
Control_Precision: 0.012
Control_Recall: 0.600

## Overall Contrast Score

Contrast_F1: 0.021
Contrast_Precision: 0.011
Contrast_Recall: 0.515
**Official Metric ->** Faithfulness: 0.997
**Official Metric ->** Consistency: 0.616

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.031
Para_Precision: 0.016
Para_Recall: 0.750
Para_Consistency: 0.505


### Numerical Paraphrase

Numerical_Para_F1: 0.000
Numerical_Para_Precision: 0.000
Numerical_Para_Recall: 0.000
Numerical_Para_Consistency: 0.589


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.996
Cont_Consistency: 0.996


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 1.000
Numerical_Cont_Consistency: 1.000


## Text_Append Scores

Text_Append_F1: 0.013
Text_Append_Precision: 0.007
Text_Append_Recall: 0.500
Text_Append_Consistency: 0.500

---

## Full Arg List

model = BioMistral/BioMistral-7B-DARE
exp_name = baseline_BioMistral-7B_0-shot_long-prompt_Greedy
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/Baseline_Prompts.json
prompt_name = Mistral7B_long-prompt
batch_size = 1
sample = False
max_new_tokens = 10
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/BioMistral-7B_0-shot_long-prompt_Greedy/
random_seed = 0

---

