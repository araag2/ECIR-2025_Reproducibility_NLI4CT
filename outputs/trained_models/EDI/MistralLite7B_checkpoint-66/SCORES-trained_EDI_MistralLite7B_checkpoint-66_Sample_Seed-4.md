# Full Evaluation Scores

File name: trained_EDI_MistralLite7B_checkpoint-66_Sample_Seed-4.json


---

## Leaderboard Scores

Metrics (%): F1-Score | Faithfulness | Consistency | Average
                79.7        72.5          70.0        74.1

---

## Overall Control Score

**Official Metric ->** Control_F1: 0.797
Control_Precision: 0.856
Control_Recall: 0.746

## Overall Contrast Score

Contrast_F1: 0.584
Contrast_Precision: 0.651
Contrast_Recall: 0.529
**Official Metric ->** Faithfulness: 0.725
**Official Metric ->** Consistency: 0.700

---


## Paraphrase Scores


### Text Paraphrase

Para_F1: 0.745
Para_Precision: 0.789
Para_Recall: 0.706
Para_Consistency: 0.730


### Numerical Paraphrase

Numerical_Para_F1: 0.604
Numerical_Para_Precision: 0.604
Numerical_Para_Recall: 0.604
Numerical_Para_Consistency: 0.679


## Contradiction Scores


### Text Contradiction

Cont_F1: 0.000
Cont_Precision: 0.000
Cont_Recall: 0.000
Cont_Faithfulness: 0.717
Cont_Consistency: 0.715


### Numerical Contradiction

Numerical_Cont_F1: 0.000
Numerical_Cont_Precision: 0.000
Numerical_Cont_Recall: 0.000
Numerical_Cont_Faithfulness: 0.772
Numerical_Cont_Consistency: 0.790


## Text_Append Scores

Text_Append_F1: 0.602
Text_Append_Precision: 0.519
Text_Append_Recall: 0.718
Text_Append_Consistency: 0.657

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
random_seed = 4
timestamp = 2024-10-24_16-46

---

