# Full Evaluation Scores

File name: baseline_llama3.1-8B_0-shot_short-prompt_Sample_Seed-0.json


---

## Overall Control Score

**Official Metric ->** Control_F1: 0.608
Control_Precision: 0.536
Control_Recall: 0.702

## Overall Contrast Score

Contrast_F1: 0.539
Contrast_Precision: 0.504
Contrast_Recall: 0.579
**Official Metric ->** Faithfulness: 0.869
**Official Metric ->** Consistency: 0.696

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.620
Para_Precision: 0.545
Para_Recall: 0.718
Para_Consistency: 0.665


### Numerical Paraphrase

Numerical_Para_F1: 0.473
Numerical_Para_Precision: 0.385
Numerical_Para_Recall: 0.614
Numerical_Para_Consistency: 0.652


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.872
Cont_Consistency: 0.849


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.851
Numerical_Cont_Consistency: 0.889


## Text_Append Scores

Text_Append_F1: 0.566
Text_Append_Precision: 0.477
Text_Append_Recall: 0.696
Text_Append_Consistency: 0.635

---

## Full Arg List

model = meta-llama/Llama-3.1-8B-Instruct
exp_name = baseline_llama3.1-8B_0-shot_short-prompt_Sample
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/Baseline_Prompts.json
prompt_name = llama_short-prompt
batch_size = 1
sample = True
max_new_tokens = 10
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/paper_baselines/llama3.1-8B/llama3.1-8B_0-shot_short-prompt_Sample/
random_seed = 0

---

