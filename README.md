# ECIR-2025 - A Reproducibility Study on Consistent Reasoning Methods for Clinical Trial Pairs
This repository supports the experiments reported on [[PDF]()]:

> TO:DO Official Publication Here

## Summary


<details>
<summary>Abstract</summary>
<br>
With the rapid expansion of AI in healthcare, ensuring that models can accurately and consistently reason within the medical domain is essential for enhancing clinical decision-making, as flawed or under-analysed advances could have detrimental consequences for patient health outcomes. Consistent reasoning is particularly challenging, as once a model outputs a judgment for a given medical statement, it should retain that judgment when faced with another statement that is only syntactically altered, and contrarily when other statements reflect a true semantic shift the model should adjust its judgment accordingly.In this paper, we describe the process of reproducing state-of-the-art methods for safe biomedical Natural Language Inference in Clinical Trials (NLI4CT), emphasizing challenges such as models' vulnerability to small input variations and the inherent complexity of Clinical Trial Reports (CTRs), which are primarily intended for expert interpretation. To improve the reproducibility thoroughness, we extend existing methods and explore a broader set of techniques, establishing baseline scores across several widely used models. We evaluate the reasoning capabilities of Large Language Models (LLMs) within the SemEval-2024 NLI4CT task, a task focused on robustness, serving as an ideal proxy for real-world applications. We conclude with an analysis of the results, highlighting key insights and empirical lessons that contribute to future research in this domain.
</details>

## Installation

To install our work and all its dependencies make sure you have an anaconda distribution installed and use the following commands:

  - Create and activate a new conda environment using the following commands:
  ```
  conda env update -f environment.yaml
  conda activate trec2024
  ```

## Running Experiments

To run any experiment, within the source folder just run:

```
bash scripts/<path_to_script> <CUDA_GPU_TO_USE>
```

For example, this command will run example_Mistral-7B.sh (0-shot of Mistral-7B-instructv0.2) with the flag CUDA_VISIBLE_DEVICES = 0

```
bash scripts/example_Mistral-7B.sh 0
```

It's worth to note that the first time each model is ran, their checkpoints will be downloaded from [huggingface]([url](https://huggingface.co/)), and that scripts within the **scripts/trained/** folder require a valid path to load the trained checkpoints from (automatically generated with scripts in **scripts/training/**). 

Additionaly, each script will output two files to the **outputs/** directory:

> FULL-ANSWER_<exp_name>     # A .json file with the full text generated and its Prediction label
> SCORES_<exp_name>          # A .md file containig all evaluated metrics

## Repository Structure

    .
    ├── data/                   # Dataset for SemEval-2024, augmented examples and the Pre-Process data we used 
    ├── outputs/                # Result files of each experiment, containing full outputs and metrics
      ├── models                # Our trained models were saved in this directory
    ├── scripts/                # Bash scripts for each individual experiment conducted
      ├── README.md             # A full breakdown of each experiment conducted, and their results
    ├── src/                    # All source code and the prompts used
    ├── .gitignore              # Close to default gitignore for python projects
    ├── environment.yml         # The libraries (and versions) necessary to run our code (import with conda)
    ├── LICENSE
    └── README.md


## Models Used

| Model  | Source |
|--------|--------|
| Mistral-7B-Instruct-v0.1       |     [huggingface](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.1)   |
| Mistral-7B-Instruct-v0.2       |     [huggingface](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2)   |
| BioMistral-7B                  |     [huggingface](https://huggingface.co/BioMistral/BioMistral-7B)             |
| MistralLite                    |     [huggingface](https://huggingface.co/amazon/MistralLite)                   |
| Llama-3.1-8B-Instruct          |     [huggingface](https://huggingface.co/meta-llama/Llama-3.1-8B-Instruct)     |
| SOLAR-10.7B-Instruct-v1.0      |     [huggingface](https://huggingface.co/upstage/SOLAR-10.7B-Instruct-v1.0)    |
| gemini-1.5-flash-002           |     [VertexAI](https://console.cloud.google.com/vertex-ai/studio/freeform)     |
| gemini-1.5-pro-002             |     [VertexAI](https://console.cloud.google.com/vertex-ai/studio/freeform)     | 

## Reproducibility experiments

For a full breakdown on the obtained results, consult [the Scripts README file](scripts/README.md)

## Acknowledgments

This research was supported by the Portuguese Recovery and Resilience Plan through project C645008882-00000055 (i.e., the Center For Responsible AI), and also by Fundação para a Ciência e Tecnologia (FCT), through the project with reference UIDB/50021/2020 (DOI:10.54499/UIDB/50021/2020). We also thank the organizers that coordinated and all the teams that participated in the SemEval-2024 NLI4CT Task, especially the ones whose work was used in this paper and had the sympathy to publicly share their code.

### SemEval-2024 Works Cited and Code Used in this Repository

#### [Edinburgh Clinical NLP at SemEval-2024 Task 2: Fine-tune your model unless you have access to GPT-4](https://aclanthology.org/2024.semeval-1.265/) | [Github Code](https://github.com/EdinburghClinicalNLP/semeval_nli4ct)

```
@inproceedings{gema-etal-2024-edinburgh,
    title = "{E}dinburgh Clinical {NLP} at {S}em{E}val-2024 Task 2: Fine-tune your model unless you have access to {GPT}-4",
    author = "Gema, Aryo  and
      Hong, Giwon  and
      Minervini, Pasquale  and
      Daines, Luke  and
      Alex, Beatrice",
    editor = {Ojha, Atul Kr.  and
      Do{\u{g}}ru{\"o}z, A. Seza  and
      Tayyar Madabushi, Harish  and
      Da San Martino, Giovanni  and
      Rosenthal, Sara  and
      Ros{\'a}, Aiala},
    booktitle = "Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)",
    month = jun,
    year = "2024",
    address = "Mexico City, Mexico",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.semeval-1.265",
    doi = "10.18653/v1/2024.semeval-1.265",
    pages = "1894--1904",
}
```

#### [NYCU-NLP at SemEval-2024 Task 2: Aggregating Large Language Models in Biomedical Natural Language Inference for Clinical Trials](https://aclanthology.org/2024.semeval-1.209/) | [Github Code]()

```
@inproceedings{lee-etal-2024-nycu,
    title = "{NYCU}-{NLP} at {S}em{E}val-2024 Task 2: Aggregating Large Language Models in Biomedical Natural Language Inference for Clinical Trials",
    author = "Lee, Lung-hao  and
      Chiou, Chen-ya  and
      Lin, Tzu-mi",
    editor = {Ojha, Atul Kr.  and
      Do{\u{g}}ru{\"o}z, A. Seza  and
      Tayyar Madabushi, Harish  and
      Da San Martino, Giovanni  and
      Rosenthal, Sara  and
      Ros{\'a}, Aiala},
    booktitle = "Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)",
    month = jun,
    year = "2024",
    address = "Mexico City, Mexico",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.semeval-1.209",
    doi = "10.18653/v1/2024.semeval-1.209",
    pages = "1455--1462",
}
```

#### [FZI-WIM at SemEval-2024 Task 2: Self-Consistent CoT for Complex NLI in Biomedical Domain](https://aclanthology.org/2024.semeval-1.184/) | [Github Code](https://github.com/jens5588/FZI-WIM-NLI4CT)

```
@inproceedings{liu-thoma-2024-fzi,
    title = "{FZI}-{WIM} at {S}em{E}val-2024 Task 2: Self-Consistent {C}o{T} for Complex {NLI} in Biomedical Domain",
    author = "Liu, Jin  and
      Thoma, Steffen",
    editor = {Ojha, Atul Kr.  and
      Do{\u{g}}ru{\"o}z, A. Seza  and
      Tayyar Madabushi, Harish  and
      Da San Martino, Giovanni  and
      Rosenthal, Sara  and
      Ros{\'a}, Aiala},
    booktitle = "Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)",
    month = jun,
    year = "2024",
    address = "Mexico City, Mexico",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.semeval-1.184",
    doi = "10.18653/v1/2024.semeval-1.184",
    pages = "1269--1279",
}
```

#### [Lisbon Computational Linguists at SemEval-2024 Task 2: Using a Mistral-7B Model and Data Augmentation](https://aclanthology.org/2024.semeval-1.185/) | [Github Code](https://github.com/araag2/SemEval2024-Task2)

```
@inproceedings{guimaraes-etal-2024-lisbon,
    title = "Lisbon Computational Linguists at {S}em{E}val-2024 Task 2: Using a Mistral-7{B} Model and Data Augmentation",
    author = "Guimar{\~a}es, Artur  and
      Martins, Bruno  and
      Magalh{\~a}es, Jo{\~a}o",
    editor = {Ojha, Atul Kr.  and
      Do{\u{g}}ru{\"o}z, A. Seza  and
      Tayyar Madabushi, Harish  and
      Da San Martino, Giovanni  and
      Rosenthal, Sara  and
      Ros{\'a}, Aiala},
    booktitle = "Proceedings of the 18th International Workshop on Semantic Evaluation (SemEval-2024)",
    month = jun,
    year = "2024",
    address = "Mexico City, Mexico",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2024.semeval-1.185",
    doi = "10.18653/v1/2024.semeval-1.185",
    pages = "1280--1287",
}
```

## Citation

TO:DO

```
@inproceedings{,
  author =    {},
  title =     {},
  booktitle = {},
  series =    {},
  pages =     {}
  year =      {},
  doi =       {},
  publisher = {}
}
```

## Contact

Should you have any questions, please contact `Artur Guimarães` at `artur.guimas@gmail.com`
