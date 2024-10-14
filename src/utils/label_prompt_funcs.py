import json
import typing

# Local Files
from .file_utils import safe_open_w

ENTAILMENT_LABELS = {"entailment", "entails", "entailed", "yes", "(yes)"}
CONTRADICTION_LABELS = {"contradiction", "contradicts", "contradicted", "no", "(no)", "✗"}

NEG_LABELS = {"not", "no", "isn't"}
CONJ_LABELS = {"a", "directly", "necessarily"}

def textlabelgroup_2_binarylabel(group_split_texts: list[list[str]]) -> int:
    answers = []
    for text_label in group_split_texts:
        text_label = [text.lower() for text in text_label]
        for i in range(len(text_label)):
            if text_label[i] in ENTAILMENT_LABELS:
                if (i > 2 and text_label[i-2] in NEG_LABELS and text_label[i-1] in CONJ_LABELS) or (i>1 and text_label[i-1] in NEG_LABELS):
                    answers.append(0)
                answers.append(1)
                break
            elif text_label[i] in CONTRADICTION_LABELS:
                if (i > 2 and text_label[i-2] in NEG_LABELS and text_label[i-1] in CONJ_LABELS) or (i>1 and text_label[i-1] in NEG_LABELS):
                    answers.append(1)
                answers.append(0)
                break
    return answers.count(1) >= answers.count(0)

def textlabel_2_binarylabel(text_label: list[str]) -> int:
    text_label = [text.lower() for text in text_label]
    for i in range(len(text_label)):
        if text_label[i] in ENTAILMENT_LABELS:
            if (i > 2 and text_label[i-2] in NEG_LABELS and text_label[i-1] in CONJ_LABELS) or (i>1 and text_label[i-1] in NEG_LABELS):
                return 0
            return 1
        elif text_label[i] in CONTRADICTION_LABELS:
            if (i > 2 and text_label[i-2] in NEG_LABELS and text_label[i-1] in CONJ_LABELS) or (i>1 and text_label[i-1] in NEG_LABELS):
                return 1
            return 0
    return 1 # In case of no label, default to Entailment

def label_2_SemEval2024(labels : dict) -> dict:
    return {q_id : {"Prediction" : "Entailment" if labels[q_id] == 1 else "Contradiction"} for q_id in labels}

# Base queries and prompts

TASK_TYPES = {"base" : [], "icl_inference_1-shot" : ["icl_1"], "icl_inference_2-shot" : ["icl_1", "icl_2"]}

def extract_info_from_query(query : dict, task_type : str = "base") -> dict:
    relevant_info = {}
    relevant_info["hypothesis"] = query["Statement"]
    relevant_info["primary_evidence"] = query["Primary_id_txt"]
    relevant_info["secondary_evidence"] = query["Secondary_id_txt"] if "Secondary_id_txt" in query else ""
    if task_type in TASK_TYPES:
        for field in TASK_TYPES[task_type]:
            #TODO: Check which field is the correct one
            relevant_info[field] = query[field] if field in query else ""
    return relevant_info

def generate_query_from_prompt(text_to_replace: dict, prompt: str, task_type : str = "base") -> str:
    prompt = prompt.replace("$primary_evidence", text_to_replace["primary_evidence"])
    if text_to_replace["secondary_evidence"] != "":
        prompt = prompt.replace("$secondary_evidence", text_to_replace["secondary_evidence"])
    else:
        prompt = prompt.replace("\nSecondary Trial:\n$secondary_evidence\n", "")
    prompt = prompt.replace("$hypothesis", text_to_replace["hypothesis"])
    if task_type in TASK_TYPES:
        for field in TASK_TYPES[task_type]:
            prompt = prompt.replace(f"${field}", text_to_replace[field])
    return prompt

def create_qid_prompt_label_dict(queries : dict, qrels : dict, prompt : str, task_type : str = "base") -> dict:
    queries_dict = {}
    for q_id in queries:
        queries_dict[q_id] = { 
            "text" : generate_query_from_prompt(extract_info_from_query(queries[q_id], task_type), prompt, task_type), 
            "gold_label" : textlabel_2_binarylabel([qrels[q_id]["Label"].strip()])
        }
    return queries_dict

def create_qdid_prompt(queries : dict, prompt : str, args : object = None) -> dict:
    queries_dict = {}

    if args and "icl_source" in vars(args) and args.icl_source != "":
        icl_source = json.load(open(args.icl_source))

        for q_id in queries:
            queries[q_id]["icl_1"] = icl_source[q_id]["icl_1"]
            queries[q_id]["icl_2"] = icl_source[q_id]["icl_2"]

    for q_id in queries:
        queries_dict[q_id] = {"text" : generate_query_from_prompt(extract_info_from_query(queries[q_id], args.task_type), prompt, args.task_type)}
    return queries_dict