import os
import json
import argparse
import pathlib

from tqdm import tqdm
from .SemEval2024_sourceEval import calc_scores
from .SemEval2024_oldEval import calc_scores_old
from ..utils.file_utils import safe_open_w


def compare_res(base_dir : pathlib.Path):
    res = {}
    files = {}

    def recursively_list_dir(curr_dir : pathlib.Path):
        for f in pathlib.Path(curr_dir).iterdir():
            if f.is_file():
                if ".md" in str(f):
                    file_read = open(f, 'r').readlines()
                    metrics = [float(s.strip()) for s in file_read[10].split()]

                    if str(f).replace("Recalc", "").replace("Original", "") not in files:
                        files[str(f).replace("Recalc", "").replace("Original", "")] = {}

                    if "Recalc" in str(f):
                        files[str(f).replace("Recalc", "")]["recalc_file"] = metrics
                    else:
                        files[str(f).replace("Original", "")]["og_file"] = metrics

            elif "models" not in str(f) or "trained_models" in str(f):
                recursively_list_dir(f)

    recursively_list_dir(base_dir)

    for file in files:
        og_file = files[file]["og_file"]
        recalc_file = files[file]["recalc_file"]

        consistency_diff = round(recalc_file[2] - og_file[2], 1)
        consistency_string = f'\\colorbox{{SpringGreen}}{{{recalc_file[2]}}} (+{consistency_diff})' if consistency_diff > 0 else f'\\colorbox{{Apricot}}{{{recalc_file[2]}}} (-{consistency_diff})'
        total_diff = round(recalc_file[3] - og_file[3], 1)
        total_string = f'\\colorbox{{SpringGreen}}{{{recalc_file[3]}}} (+{total_diff})' if consistency_diff > 0 else f'\\colorbox{{Apricot}}{{{recalc_file[3]}}} (-{total_diff})'
        res[str(file)] = f'{consistency_string} & {total_string}'

    print(res)

    with safe_open_w("../quick_res.json") as out:
        out.write(json.dumps(res, ensure_ascii=False, indent=4))
    


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--base_dir', default='')
    args = parser.parse_args()

    files = []
    def recursively_list_dir(curr_dir : pathlib.Path):
        for f in pathlib.Path(curr_dir).iterdir():
            if f.is_file():
                if ".md" in str(f) or ".txt" in str(f):
                    os.remove(f)

                if ".json" in str(f):
                    split_path = str(f).split("/")
                    og_file_link, path, name = str(f), "/".join(split_path[:-1])+"/", split_path[-1].replace("FULL-ANSWERS_", "Recalc-")
                    files.append((og_file_link, path, name))
                    og_file_link, path, name = str(f), "/".join(split_path[:-1])+"/", split_path[-1].replace("FULL-ANSWERS_", "Original-")
                    files.append((og_file_link, path, name))
    
            elif "models" not in str(f) or "trained_models" in str(f):
                recursively_list_dir(f)
    
    recursively_list_dir(pathlib.Path(args.base_dir))

    for og_file_link, file_path, file_name in tqdm(files):
        predictions = json.load(open(og_file_link))
        if "Recalc" in file_name:
            calc_scores({key : {"Prediction" : predictions[key]["label"]} for key in predictions}, file_name, file_path)
        else:
            calc_scores_old({key : {"Prediction" : predictions[key]["label"]} for key in predictions}, file_name, file_path)

    compare_res(args.base_dir)

if '__main__' == __name__:
    main()