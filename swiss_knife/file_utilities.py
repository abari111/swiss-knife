import os
from typing import Set, Dict
from pathlib import Path
from collections import Counter
import shutil

from magika import Magika

INSECURE_EXT = ["exe", "bat", ".vbs", ".vbe", "pebin"]


def check_executable(dir_path: str) -> bool:
    """
    Check suspicious executables files in directory
    """
    outputs = check_files_ext(dir_path)
    exec_files = []

    for name, label, score in zip(
        outputs["paths"], outputs["labels"], outputs["scores"]
    ):
        if label in INSECURE_EXT:
            exec_files.append((name, label, score))

    if exec_files:
        print("Executables files found")
        print(exec_files)
        return True


def check_files_ext(dir_path: str) -> Dict[str, list]:
    """
    return files extension presents in a directory
    """
    list_files = os.listdir(dir_path)
    files_path = [Path(dir_path + "/" + file_name) for file_name in list_files]

    model = Magika()
    results = model.identify_paths(files_path)
    outputs = {"paths": [], "labels": [], "scores": []}

    for res in results:
        outputs["paths"].append(res.path)
        outputs["labels"].append(res.output.ct_label)
        outputs["scores"].append(res.output.score)

    return outputs


def get_dir_files_ext(dir_path: str) -> Set[str]:
    """
    return files extension presents in a directory
    """
    list_files = os.listdir(dir_path)
    files_path = [Path(dir_path + "/" + file_name) for file_name in list_files]

    model = Magika()
    results = model.identify_paths(files_path)
    outputs = {"paths": [], "labels": [], "scores": []}

    for res in results:
        outputs["paths"] = res.path
        outputs["labels"] = res.output.ct_label
        outputs["scores"] = res.output.score

    return set(outputs["labels"])


def check_file_ext(file_path: str) -> str:
    """
    Check files extensions
    """
    with open(file_path, "rb") as file:
        file = file.read()

    model = Magika()
    res = model.identify_bytes(file)

    return res.output.ct_label


def file_analyser(dir_path: str) -> Dict:

    if not os.path.exists(dir_path):
        return None

    list_files = os.listdir(dir_path)
    files_path = [Path(dir_path + "/" + file_name) for file_name in list_files]

    model = Magika()
    results = model.identify_paths(files_path)
    files_ext = []

    for res in results:
        files_ext.append(res.output.ct_label)

    ext_counter = Counter(files_ext)

    return ext_counter


def group_file_by_ext(dir_path:str, dest_path:str=None):
    if not os.path.exists(dir_path):
        return None

    list_files = os.listdir(dir_path)
    files_path = [Path(dir_path + "/" + file_name) for file_name in list_files]

    model = Magika()
    results = model.identify_paths(files_path)
    files_ext = [res.output.ct_label for res in results]
    files_ext = set(files_ext)
    files = {ext: [] for ext in files_ext}
    for res in results:
        files[res.output.ct_label].append(res.path)
        
    os.chdir(dir_path)
    if not dest_path:
        dest_path = dir_path
        
    for key in files.keys():
        try:
            os.mkdir(key)
        except Exception as e:
            pass
        
        if not os.path.exists(key):
            raise FileNotFoundError
        
        for file_path in files[key]:
            source_filepath = file_path.split("\\")[-1]
            dest_filepath = os.path.join(key ,file_path.split("\\")[-1])
            shutil.move(source_filepath, dest_filepath)
    
    return True

if __name__ == "__main__":
    analysis_res = file_analyser("assets/MyData")
    files = group_file_by_ext("assets/MyData")

