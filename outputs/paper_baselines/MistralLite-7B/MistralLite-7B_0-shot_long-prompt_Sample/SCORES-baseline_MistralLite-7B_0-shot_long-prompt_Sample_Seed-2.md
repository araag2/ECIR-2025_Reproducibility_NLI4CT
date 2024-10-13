# Full Evaluation Scores

File name: baseline_MistralLite-7B_0-shot_long-prompt_Sample_Seed-2.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                52.8        65.2          56.6        58.2

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.528
Control_Precision: 0.508
Control_Recall: 0.550

## Overall Contrast Score

Contrast_F1: 0.423
Contrast_Precision: 0.482
Contrast_Recall: 0.376
**Official Metric ->** Faithfulness: 0.652
**Official Metric ->** Consistency: 0.566

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.532
Para_Precision: 0.508
Para_Recall: 0.559
Para_Consistency: 0.554


### Numerical Paraphrase

Numerical_Para_F1: 0.538
Numerical_Para_Precision: 0.582
Numerical_Para_Recall: 0.500
Numerical_Para_Consistency: 0.594


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.647
Cont_Consistency: 0.633


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.684
Numerical_Cont_Consistency: 0.660


## Text_Append Scores

Text_Append_F1: 0.486
Text_Append_Precision: 0.444
Text_Append_Recall: 0.536
Text_Append_Consistency: 0.530

---

## Full Arg List

model = amazon/MistralLite
exp_name = baseline_MistralLite-7B_0-shot_long-prompt_Sample
checkpoint = 
merge = False
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/Baseline_Prompts.json
prompt_name = MistralLite-7B_long-prompt
batch_size = 1
sample = True
max_new_tokens = 10
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/paper_baselines/MistralLite-7B/MistralLite-7B_0-shot_long-prompt_Sample/
random_seed = 2

---

