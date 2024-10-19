# Full Evaluation Scores

File name: icl_CoT-ver_2-shot_llama3.1-8B_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                68.5        87.0          72.8        76.1

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.685
Control_Precision: 0.608
Control_Recall: 0.784

## Overall Contrast Score

Contrast_F1: 0.603
Contrast_Precision: 0.590
Contrast_Recall: 0.616
**Official Metric ->** Faithfulness: 0.870
**Official Metric ->** Consistency: 0.728

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.677
Para_Precision: 0.608
Para_Recall: 0.763
Para_Consistency: 0.709


### Numerical Paraphrase

Numerical_Para_F1: 0.584
Numerical_Para_Precision: 0.516
Numerical_Para_Recall: 0.671
Numerical_Para_Consistency: 0.701


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.865
Cont_Consistency: 0.807


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.904
Numerical_Cont_Consistency: 0.975


## Text_Append Scores

Text_Append_F1: 0.648
Text_Append_Precision: 0.581
Text_Append_Recall: 0.732
Text_Append_Consistency: 0.684

---

## Full Arg List

model = meta-llama/Llama-3.1-8B-Instruct
exp_name = icl_CoT-ver_2-shot_llama3.1-8B
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/ICL_Prompts.json
prompt_name = icl-2_EDI-CoT-ver_llama3.1-8B_prompt
batch_size = 1
sample = False
max_new_tokens = 1000
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = icl_inference_CoT-ver_2-shot
icl_source = data/SemEval-2024/icl/icl_CoT-ver/icl_CoT-ver_EDI_GPT-4_llama3.1-8B.json
output_dir = outputs/icl_CoT-ver_2-shot/
random_seed = 0
timestamp = 2024-10-16_10-59

---

