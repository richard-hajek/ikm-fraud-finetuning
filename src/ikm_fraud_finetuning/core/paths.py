import pathlib
import os

def find_parent_with_pyproject_toml(expected_entry="pyproject.toml"):
    prev_parent = None
    p = pathlib.Path(os.getcwd())

    while p != prev_parent:
        test_file = p / expected_entry

        if test_file.exists():
            return p

        prev_parent = p
        p = p.parent

    raise Exception("Could not find the data folders")

PATH_ROOT=find_parent_with_pyproject_toml()
PATH_ARTIFACTS=PATH_ROOT / "_artifacts"
PATH_NOTEBOOKS=PATH_ROOT / "_notebooks"
PATH_OUTPUT=PATH_ROOT / "_output"