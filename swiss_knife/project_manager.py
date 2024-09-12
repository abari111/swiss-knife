import sys
import os
from collections.abc import Iterator


import pathlib
import yaml

excluded_files = ["specs"]


def _parse_yaml(
    file_name: str,
):
    with open(file_name, "r") as fd:
        data = yaml.safe_load(fd)
    return data


def generate_project_struct(file_name: str, proj_path=None):
    data = _parse_yaml(file_name)

    if proj_path:
        os.chdir(proj_path)
    else:
        cwd = os.getcwd()
        proj_path = os.path.join(cwd, "trash")
        if not os.path.exists(proj_path):
            os.mkdir(proj_path)
        os.chdir(proj_path)

    for key, val in data.items():

        if not os.path.exists(key) and key not in excluded_files:
            os.mkdir(key)
        if isinstance(val, list):
            print("yes")
            for file in val:
                if key not in excluded_files:
                    file = os.path.join(key, file)
                with open(file, "w") as fd:
                    pass
        elif not (val is None):
            with open(val, "w") as fd:
                pass


if __name__ == "__main__":
    file_name = "project-structure.yml"
    # data = _parse_yaml(file_name)
    generate_project_struct(file_name)
