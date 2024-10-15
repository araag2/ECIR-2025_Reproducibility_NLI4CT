# Full Evaluation Scores

File name: self-consistency_CoT_llama3.1-8B_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                70.1        76.3          65.8        70.7

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.701
Control_Precision: 0.712
Control_Recall: 0.690

## Overall Contrast Score

Contrast_F1: 0.595
Contrast_Precision: 0.747
Contrast_Recall: 0.494
**Official Metric ->** Faithfulness: 0.763
**Official Metric ->** Consistency: 0.658

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.696
Para_Precision: 0.737
Para_Recall: 0.658
Para_Consistency: 0.677


### Numerical Paraphrase

Numerical_Para_F1: 0.612
Numerical_Para_Precision: 0.692
Numerical_Para_Recall: 0.548
Numerical_Para_Consistency: 0.643


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.776
Cont_Consistency: 0.668


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.675
Numerical_Cont_Consistency: 0.691


## Text_Append Scores

Text_Append_F1: 0.675
Text_Append_Precision: 0.763
Text_Append_Recall: 0.606
Text_Append_Consistency: 0.633

---

## Full Arg List

model = meta-llama/Llama-3.1-8B-Instruct
exp_name = self-consistency_CoT_llama3.1-8B
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/CoT_Prompts.json
prompt_name = llama_CoT-prompt
batch_size = 2
sample = True
max_new_tokens = 500
temperature = 1.0
top_k = 50
top_p = 0.99
num_return_sequences = 5
task_type = self-consistency_CoT_inference
icl_source = 
output_dir = outputs/self-consistency_CoT/
random_seed = 0

---

