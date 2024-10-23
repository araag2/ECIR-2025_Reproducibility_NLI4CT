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
| [Gemini-1.5-flash-002](baselines/Gemini/inference_Gemini-1.5-flash.sh)                            |  long  |  Greedy   |    -     |      -       |      -      |    -    |
| [Gemini-1.5-pro-002](baselines/Gemini/inference_Gemini-1.5-pro.sh)                                |  long  |  Greedy   |    -     |      -       |      -      |    -    ||

### Reproduced Methods without Fine-Tuning

### Reproduced Methods with Fine-Tuning
