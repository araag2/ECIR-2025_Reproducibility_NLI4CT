import json
from .file_utils import safe_open_w

def from_bm25_2_icl(icl_source : dict, bm25_scores : dict, output_file : str):
    queries = json.load(open("ECIR2024_Reproducibility_TREC2024/data/SemEval-2024/icl/icl_label-only/icl_label-only_EDI_queries2024_train-dev.json"))

    source = {**json.load(open("ECIR2024_Reproducibility_TREC2024/data/SemEval-2024/icl/icl_bm25/icl_bm25_source_train.json")), **json.load(open("ECIR2024_Reproducibility_TREC2024/data/SemEval-2024/icl/icl_bm25/icl_bm25_source_test.json")), **json.load(open("ECIR2024_Reproducibility_TREC2024/data/SemEval-2024/icl/icl_bm25/icl_bm25_source_dev.json"))}

    new_dict = {}

    for key in source:
        top_contra = None
        top_contra_text = None

        for contra in source[key]["contradictions"]:
            if contra["id"] in queries:
                top_contra = contra
                top_contra_text = queries[contra["id"]]
                break

        top_entail = None
        top_entail_text = None
        for entail in source[key]["entailments"]:
            if entail["id"] in queries:
                top_entail = entail
                top_entail_text = queries[entail["id"]]
                break

        if top_contra["score"] > top_entail["score"]:
            new_dict[key] = {"icl_1" : top_contra_text, "icl_2" : top_entail_text}
        else:
            new_dict[key] = {"icl_1" : top_entail_text, "icl_2" : top_contra_text}

    with safe_open_w(f'ECIR2024_Reproducibility_TREC2024/data/SemEval-2024/icl/icl_label-only/icl_label-only_EDI.json') as output_file:
        output_file.write(json.dumps(new_dict, ensure_ascii=False, indent=4))


def main():
    queries = json.load(open("ECIR2024_Reproducibility_TREC2024/data/SemEval-2024/icl/icl_label-only/icl_label-only_EDI_queries2024_train-dev.json"))

    source = {**json.load(open("ECIR2024_Reproducibility_TREC2024/data/SemEval-2024/icl/icl_bm25/icl_bm25_source_train.json")), **json.load(open("ECIR2024_Reproducibility_TREC2024/data/SemEval-2024/icl/icl_bm25/icl_bm25_source_test.json")), **json.load(open("ECIR2024_Reproducibility_TREC2024/data/SemEval-2024/icl/icl_bm25/icl_bm25_source_dev.json"))}

    new_dict = {}

    for key in source:
        top_contra = None
        top_contra_text = None

        for contra in source[key]["contradictions"]:
            if contra["id"] in queries:
                top_contra = contra
                top_contra_text = queries[contra["id"]]
                break

        top_entail = None
        top_entail_text = None
        for entail in source[key]["entailments"]:
            if entail["id"] in queries:
                top_entail = entail
                top_entail_text = queries[entail["id"]]
                break

        if top_contra["score"] > top_entail["score"]:
            new_dict[key] = {"icl_1" : top_contra_text, "icl_2" : top_entail_text}
        else:
            new_dict[key] = {"icl_1" : top_entail_text, "icl_2" : top_contra_text}

    with safe_open_w(f'ECIR2024_Reproducibility_TREC2024/data/SemEval-2024/icl/icl_label-only/icl_label-only_EDI.json') as output_file:
        output_file.write(json.dumps(new_dict, ensure_ascii=False, indent=4))

if __name__ == '__main__':
    main()