# Full Evaluation Scores

File name: trained_EDI_MistralLite7B_checkpoint-66_Sample_Seed-2.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                80.4        72.8          70.2        74.5

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.804
Control_Precision: 0.868
Control_Recall: 0.748

## Overall Contrast Score

Contrast_F1: 0.589
Contrast_Precision: 0.661
Contrast_Recall: 0.532
**Official Metric ->** Faithfulness: 0.728
**Official Metric ->** Consistency: 0.702

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.747
Para_Precision: 0.793
Para_Recall: 0.706
Para_Consistency: 0.731


### Numerical Paraphrase

Numerical_Para_F1: 0.590
Numerical_Para_Precision: 0.593
Numerical_Para_Recall: 0.587
Numerical_Para_Consistency: 0.665


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.724
Cont_Consistency: 0.709


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.754
Numerical_Cont_Consistency: 0.815


## Text_Append Scores

Text_Append_F1: 0.614
Text_Append_Precision: 0.536
Text_Append_Recall: 0.719
Text_Append_Consistency: 0.663

---

## Full Arg List

model = amazon/MistralLite
exp_name = trained_EDI_MistralLite7B_checkpoint-66_Sample
checkpoint = outputs/models/trained-EDI_MistralLite_true-dropout/checkpoint-66
used_set = test
queries = data/SemEval-2024/queries/queries2024_test.json
qrels = data/SemEval-2024/qrels/qrels2024_test.json
prompt_file = src/prompts/EDI_Prompts.json
prompt_name = EDI_MistralLite_prompt
batch_size = 8
sample = True
max_new_tokens = 10
temperature = 0.5
top_k = 15
top_p = 0.7
num_return_sequences = 1
task_type = base_inference
icl_source = 
output_dir = outputs/trained_models/EDI/MistralLite7B_checkpoint-66/
random_seed = 2
timestamp = 2024-10-24_16-00

---

