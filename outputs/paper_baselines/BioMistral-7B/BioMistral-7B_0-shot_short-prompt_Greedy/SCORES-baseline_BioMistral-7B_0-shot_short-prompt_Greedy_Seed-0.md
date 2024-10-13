# Full Evaluation Scores

File name: baseline_BioMistral-7B_0-shot_short-prompt_Greedy_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                61.3        55.0          56.1        57.5

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.613
Control_Precision: 0.684
Control_Recall: 0.555

## Overall Contrast Score

Contrast_F1: 0.473
Contrast_Precision: 0.622
Contrast_Recall: 0.382
**Official Metric ->** Faithfulness: 0.550
**Official Metric ->** Consistency: 0.561

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.618
Para_Precision: 0.667
Para_Recall: 0.576
Para_Consistency: 0.588


### Numerical Paraphrase

Numerical_Para_F1: 0.551
Numerical_Para_Precision: 0.648
Numerical_Para_Recall: 0.480
Numerical_Para_Consistency: 0.571


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.549
Cont_Consistency: 0.580


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.553
Numerical_Cont_Consistency: 0.500


## Text_Append Scores

Text_Append_F1: 0.550
Text_Append_Precision: 0.575
Text_Append_Recall: 0.527
Text_Append_Consistency: 0.529

---

## Full Arg List

model = BioMistral/BioMistral-7B-DARE
exp_name = baseline_BioMistral-7B_0-shot_short-prompt_Greedy
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/Baseline_Prompts.json
prompt_name = Mistral7B_short-prompt
batch_size = 1
sample = False
max_new_tokens = 10
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/
random_seed = 0

---

