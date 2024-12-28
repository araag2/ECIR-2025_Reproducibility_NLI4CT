## Reproducibility Experiments

### Baselines

| Model               | Prompt | Text Gen  | F1-Score | Faithfulness | Consistency | Average |
|---------------------|:------:|:---------:|:--------:|:------------:|:-----------:|:-------:|
| [Mistral-7B-Instruct](baselines/Mistral-7B/inference_Mistral-7B_0-shot_short-prompt_Greedy.sh)    | short  |  Greedy   |   72.4   |     70.9     |    65.2     |  69.5   |
| [Mistral-7B-Instruct](baselines/Mistral-7B/inference_Mistral-7B_0-shot_short-prompt_Sample.sh)    | short  | Sampling  |   72.1   |     71.3     |    65.0     |  69.5   |
| [Mistral-7B-Instruct](baselines/Mistral-7B/inference_Mistral-7B_0-shot_long-prompt_Greedy.sh)     |  long  |  Greedy   |   70.6   |     56.6     |    62.0     |  63.1   |
| [Mistral-7B-Instruct](baselines/Mistral-7B/inference_Mistral-7B_0-shot_long-prompt_Sample.sh)     |  long  | Sampling  |   70.6   |     56.7     |    61.7     |  63.0   |
| [BioMistral-7B](baselines/BioMistral-7B/inference_BioMistral-7B_0-shot_short-prompt_Greedy.sh)    | short  |  Greedy   |   61.3   |     55.0     |    56.1     |  57.5   |
| [BioMistral-7B](baselines/BioMistral-7B/inference_BioMistral-7B_0-shot_short-prompt_Sample.sh)    | short  | Sampling  |   64.3   |     49.4     |    53.7     |  55.8   |
| [BioMistral-7B](baselines/BioMistral-7B/inference_BioMistral-7B_0-shot_long-prompt_Greedy.sh)     |  long  |  Greedy   |   2.4    |     99.7     |    61.6     |  54.6   |
| [BioMistral-7B](baselines/BioMistral-7B/inference_BioMistral-7B_0-shot_long-prompt_Sample.sh)     |  long  | Sampling  |   39.3   |     80.3     |    57.5     |  59.0   |
| [MistralLite-7B](baselines/MistralLite-7B/inference_MistralLite-7B_0-shot_short-prompt_Greedy.sh) | short  |  Greedy   |   33.8   |     89.5     |    61.6     |  61.6   |
| [MistralLite-7B](baselines/MistralLite-7B/inference_MistralLite-7B_0-shot_short-prompt_Sample.sh) | short  | Sampling  |   42.5   |     83.9     |    58.9     |  61.8   |
| [MistralLite-7B](baselines/MistralLite-7B/inference_MistralLite-7B_0-shot_long-prompt_Greedy.sh)  |  long  |  Greedy   |   58.0   |     68.4     |    59.4     |  61.9   |
| [MistralLite-7B](baselines/MistralLite-7B/inference_MistralLite-7B_0-shot_long-prompt_Sample.sh)  |  long  | Sampling  |   53.7   |     68.4     |    56.9     |  59.7   |
| [llama3.1-8B-instruct](baselines/llama3.1-8B/inference_llama3.1-8B_0-shot_short-prompt_Greedy.sh) | short  |  Greedy   |   59.0   |     87.5     |    69.7     |  72.1   |
| [llama3.1-8B-instruct](baselines/llama3.1-8B/inference_llama3.1-8B_0-shot_short-prompt_Sample.sh) | short  | Sampling  |   61.7   |     86.2     |    69.6     |  72.5   |
| [llama3.1-8B-instruct](baselines/llama3.1-8B/inference_llama3.1-8B_0-shot_long-prompt_Greedy.sh)  |  long  |  Greedy   |   67.5   |     80.3     |    69.2     |  72.3   |
| [llama3.1-8B-instruct](baselines/llama3.1-8B/inference_llama3.1-8B_0-shot_long-prompt_Sample.sh)  |  long  | Sampling  |   67.4   |     79.6     |    68.7     |  71.9   |
| [Gemini-1.5-flash-001](baselines/Gemini/inference_Gemini-1.5-flash.sh)                            |  short |  Greedy   |   75.5   |     86.3     |    75.2     |  79.0   |
| [Gemini-1.5-flash-001](baselines/Gemini/inference_Gemini-1.5-flash.sh)                            |  long  |  Greedy   |   71.6   |     84.7     |    71.8     |  76.0   |
| [Gemini-1.5-flash-001](baselines/Gemini/inference_Gemini-1.5-flash.sh)                            |  short |  Greedy   |   **76.6**   |    ** 92.6**       |      **77.7**      |    **82.3**    |
| [Gemini-1.5-pro-001](baselines/Gemini/inference_Gemini-1.5-pro.sh)                                |  long  |  Greedy   |    73.6    |     92.1       |     74.1     |    79.9   |

### Reproduced Methods without Fine-Tuning

We can find the scripts these models by category, 0-shot within the [Baselines](baselines/), Chain-of-thought in the [CoT](CoT/), 1-sho, 2-shot and CoT + 1-shot/2-shot in the [ICL Folder](icl_inference/).

| **Original Model / Our Model**                         |         | **Technique** |         | **F1**                 |         | **Faith.**               |         | **Consist.**              |         | **Avg.**                |
|--------------------------------------------------------|---------|:---------------:|---------|:-------------------------:|---------|:---------------------------:|---------|:---------------------------:|---------|:--------------------------:|
| Mistral-7B-Inst. / Mistral-7B-Inst. [1]                                     |         | 0-shot       |         | 65.3 / <span style="background-color: SpringGreen">72.4</span> |         | 13.4 / <span style="background-color: SpringGreen">70.9</span> |         | 41.5 / <span style="background-color: SpringGreen">65.2</span> |         | 40.1 / <span style="background-color: SpringGreen">69.5</span> |
|                                                        |         | 1-shot       |         | 66.4 / <span style="background-color: Apricot">48.8</span> |         | 11.1 / <span style="background-color: SpringGreen">88.3</span> |         | 41.3 / <span style="background-color: SpringGreen">65.2</span> |         | 39.6 / <span style="background-color: SpringGreen">67.4</span> |
|                                                        |         | 2-shot       |         | 66.9 / <span style="background-color: Apricot">51.1</span> |         | 13.4 / <span style="background-color: SpringGreen">86.3</span> |         | 42.5 / <span style="background-color: SpringGreen">65.7</span> |         | 40.9 / <span style="background-color: SpringGreen">67.7</span> |
|                                                        |         | CoT          |         | 47.1 / <span style="background-color: SpringGreen">48.2</span> |         | 59.3 / <span style="background-color: SpringGreen">79.6</span> |         | 50.8 / <span style="background-color: SpringGreen">60.5</span> |         | 52.4 / <span style="background-color: SpringGreen">62.8</span> |
|                                                        |         | CoT+1-shot   |         | 58.4 / <span style="background-color: SpringGreen">69.4</span> |         | 57.1 / <span style="background-color: SpringGreen">84.7</span> |         | 54.9 / <span style="background-color: SpringGreen">71.3</span> |         | 56.8 / <span style="background-color: SpringGreen">75.1</span> |
|                                                        |         | CoT+2-shot   |         | 59.4 / <span style="background-color: SpringGreen">59.5</span> |         | 60.7 / <span style="background-color: Apricot">77.5</span> |         | 56.5 / <span style="background-color: SpringGreen">63.7</span> |         | 58.9 / <span style="background-color: SpringGreen">66.9</span> |                         |
| LLaMA2-13B / LLaMa3.1-8B [1]                                          |         | 0-shot       |         | 60.7 / <span style="background-color: SpringGreen">67.5</span> |         | 45.0 / <span style="background-color: SpringGreen">80.3</span> |         | 49.4 / <span style="background-color: SpringGreen">69.2</span> |         | 51.7 / <span style="background-color: SpringGreen">72.3</span> |
|                                                        |         | 1-shot       |         | 63.0 / <span style="background-color: SpringGreen">69.0</span> |         | 33.5 / <span style="background-color: SpringGreen">80.9</span> |         | 48.8 / <span style="background-color: SpringGreen">69.1</span> |         | 48.4 / <span style="background-color: SpringGreen">73.0</span> |
|                                                        |         | 2-shot       |         | 61.7 / <span style="background-color: SpringGreen">70.2</span> |         | 40.2 / <span style="background-color: SpringGreen">74.3</span> |         | 50.1 / <span style="background-color: SpringGreen">68.1</span> |         | 50.7 / <span style="background-color: SpringGreen">70.9</span> |
|                                                        |         | CoT          |         | 60.3 / <span style="background-color: SpringGreen">64.5</span> |         | 50.1 / <span style="background-color: SpringGreen">88.2</span> |         | 51.2 / <span style="background-color: SpringGreen">68.3</span> |         | 53.9 / <span style="background-color: SpringGreen">73.7</span> |
|                                                        |         | CoT+1-shot   |         | 63.5 / <span style="background-color: SpringGreen">69.4</span> |         | 53.1 / <span style="background-color: SpringGreen">84.7</span> |         | 53.6 / <span style="background-color: SpringGreen">71.3</span> |         | 56.7 / <span style="background-color: SpringGreen">75.1</span> |
|                                                        |         | CoT+2-shot   |         | 59.2 / <span style="background-color: SpringGreen">68.5</span> |         | 61.2 / <span style="background-color: SpringGreen">87.0</span> |         | 55.5 / <span style="background-color: SpringGreen">72.8</span> |         | 58.6 / <span style="background-color: SpringGreen">76.1</span> |
| Mistral-7B-Inst. / Mistral-7B-Inst. [2]                                     |         | 0-shot       |         | 67.3 / <span style="background-color: SpringGreen">70.6</span> |         | 61.8 / <span style="background-color: Apricot">56.7</span> |         | 53.8 / <span style="background-color: SpringGreen">61.7</span> |         | 60.1 / <span style="background-color: SpringGreen">63.0</span> |
| GPT-4 [1] / Gemini                                               |         | 0-shot       |         | 77.5 / 76.6                  |         | 94.8 / 92.6                   |         | 77.5 / <span style="background-color: SpringGreen">77.7</span>                   |         | 83.3 / 82.3                  |

### Reproduced Methods with Fine-Tuning

After training models with [Training Scripts](training/), you can obtain these results by running [Trained Models](trained_models/) scripts. All folders are divided by team names.


| Original Model /Our Model | Technique    |           | F1                      |           | Faith.                     |           | Consist.                    |           | Avg.                        |
|----------------------------|:--------------:|-----------|:--------------------------:|-----------|:----------------------------:|-----------|:-----------------------------:|-----------|:-----------------------------:|
| Mistral-7B-Inst. [1] /Mistral-7B-Inst. | -          |           | 76.9 / 78.7    |           | 76.6 / 85.1        |           | 71.4 / 70.8         |           | 75.0 / 78.2         |
|                              |              |           |                          |           |                            |           |                             |           |                             |
| MistralLite-7B [1] /MistralLite-7B | - |           | 74.8 / 79.1       |           | 87.3 / 73.8        |           | 72.2 / 70.5         |           | 78.1 / 74.5         |
|                              |              |           |                          |           |                            |           |                             |           |                             |
| LLaMA2-13B [1] /LLaMa3.1-8B | -          |           | 67.7 / 81.0      |           | 77.3 / 73.6        |           | 66.1 / 73.7         |           | 70.4 / 76.1         |
| Mistral-7B-Inst. [2] /Mistral-7B-Inst. | -          |           | 81.2 / 80.5   |           | 72.3 / 79.1        |           | 69.2 / 70.5         |           | 74.2 / 76.7         |
|                              | Manual Aug. |           | 82.9 / 77.6      |           | 76.9 / 83.4        |           | 71.9 / 69.9         |           | 77.2 / 77.0         |
|                              | Synth. Aug. |           | 78.1 / 77.8      |           | 78.0 / 85.6        |           | 71.0 / 70.8         |           | 75.7 / 78.1         |
|                              | Mix Aug.    |           | 80.1 / 80.5      |           | 83.1 / 79.3        |           | 72.2 / 73.8         |           | 78.5 / 77.9         |
| Mixtral-8x7B [3] /Mistral-7B-Inst. | -  |           | 78.7 / 79.5      |           | 81.0 / 78.9        |           | 73.6 / 70.3         |           | 77.8 / 76.3         |
|                              | CoT         |           | 78.7 / 73.9      |           | 89.7 / 84.7        |           | 72.2 / 69.7         |           | 80.2 / 76.1         |
|                              | CoT+SC      |           | 80.0 / 79.0      |           | 90.4 / 84.0        |           | 72.9 / 69.1         |           | 81.1 / 77.4         |
| Mistral-7B [4] / -           | Reduction   |           | 76.2 / --------         |           | 86.1 / --------           |           | 78.1 / --------            |           | 80.1 / --------            |
| Solar-10.7B [4] / -          | Reduction   |           | 77.9 / --------         |           | 92.4 / --------           |           | 80.9 / --------            |           | 83.7 / --------            |

References:  
- [1] [Gema et al., 2024 - Edinburgh](https://aclanthology.org/2024.semeval-1.265/)
- [2] [Guimaraes, 2024 - Lisbon](https://aclanthology.org/2024.semeval-1.185/)  
- [3] [Liu & Thoma, 2024 - FZI ](https://aclanthology.org/2024.semeval-1.184/) 
- [4] [Lee et al., 2024 - NYCU](https://aclanthology.org/2024.semeval-1.209/)  


