# Full Evaluation Scores

File name: CoT_llama3.1-8B_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                67.1        76.6          65.0        69.6

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.671
Control_Precision: 0.644
Control_Recall: 0.700

## Overall Contrast Score

Contrast_F1: 0.558
Contrast_Precision: 0.654
Contrast_Recall: 0.487
**Official Metric ->** Faithfulness: 0.766
**Official Metric ->** Consistency: 0.650

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.637
Para_Precision: 0.633
Para_Recall: 0.640
Para_Consistency: 0.639


### Numerical Paraphrase

Numerical_Para_F1: 0.538
Numerical_Para_Precision: 0.549
Numerical_Para_Recall: 0.526
Numerical_Para_Consistency: 0.616


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.767
Cont_Consistency: 0.704


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.763
Numerical_Cont_Consistency: 0.759


## Text_Append Scores

Text_Append_F1: 0.649
Text_Append_Precision: 0.688
Text_Append_Recall: 0.615
Text_Append_Consistency: 0.629

---

## Full Arg List

model = meta-llama/Llama-3.1-8B-Instruct
exp_name = CoT_llama3.1-8B
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/CoT_Prompts.json
prompt_name = llama_CoT-prompt
batch_size = 8
sample = False
max_new_tokens = 1000
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = CoT_inference
icl_source = 
output_dir = outputs/CoT/
random_seed = 0

---
