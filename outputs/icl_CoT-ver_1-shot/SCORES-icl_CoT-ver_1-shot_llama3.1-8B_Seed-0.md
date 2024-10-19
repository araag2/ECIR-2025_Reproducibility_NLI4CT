# Full Evaluation Scores

File name: icl_CoT-ver_1-shot_llama3.1-8B_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                69.4        84.7          71.3        75.1

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.694
Control_Precision: 0.616
Control_Recall: 0.794

## Overall Contrast Score

Contrast_F1: 0.594
Contrast_Precision: 0.608
Contrast_Recall: 0.581
**Official Metric ->** Faithfulness: 0.847
**Official Metric ->** Consistency: 0.713

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.650
Para_Precision: 0.593
Para_Recall: 0.719
Para_Consistency: 0.681


### Numerical Paraphrase

Numerical_Para_F1: 0.566
Numerical_Para_Precision: 0.538
Numerical_Para_Recall: 0.598
Numerical_Para_Consistency: 0.665


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.849
Cont_Consistency: 0.785


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.833
Numerical_Cont_Consistency: 0.870


## Text_Append Scores

Text_Append_F1: 0.677
Text_Append_Precision: 0.631
Text_Append_Recall: 0.730
Text_Append_Consistency: 0.699

---

## Full Arg List

model = meta-llama/Llama-3.1-8B-Instruct
exp_name = icl_CoT-ver_1-shot_llama3.1-8B
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/ICL_Prompts.json
prompt_name = icl-1_EDI-CoT-ver_llama3.1-8B_prompt
batch_size = 1
sample = False
max_new_tokens = 500
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = icl_inference_CoT-ver_1-shot
icl_source = data/SemEval-2024/icl/icl_CoT-ver/icl_CoT-ver_EDI_GPT-4_llama3.1-8B.json
output_dir = outputs/icl_CoT-ver_1-shot/
random_seed = 0
timestamp = 2024-10-17_13-40

---

