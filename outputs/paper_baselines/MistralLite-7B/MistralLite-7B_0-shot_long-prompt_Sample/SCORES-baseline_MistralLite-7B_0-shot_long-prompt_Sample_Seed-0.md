# Full Evaluation Scores

File name: baseline_MistralLite-7B_0-shot_long-prompt_Sample_Seed-0.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                53.7        68.4          56.9        59.6

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.537
Control_Precision: 0.512
Control_Recall: 0.564

## Overall Contrast Score

Contrast_F1: 0.418
Contrast_Precision: 0.465
Contrast_Recall: 0.380
**Official Metric ->** Faithfulness: 0.684
**Official Metric ->** Consistency: 0.569

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.524
Para_Precision: 0.504
Para_Recall: 0.546
Para_Consistency: 0.543


### Numerical Paraphrase

Numerical_Para_F1: 0.433
Numerical_Para_Precision: 0.429
Numerical_Para_Recall: 0.438
Numerical_Para_Consistency: 0.545


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.688
Cont_Consistency: 0.691


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.658
Numerical_Cont_Consistency: 0.679


## Text_Append Scores

Text_Append_F1: 0.476
Text_Append_Precision: 0.431
Text_Append_Recall: 0.531
Text_Append_Consistency: 0.525

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
random_seed = 0

---

