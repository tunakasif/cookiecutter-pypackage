from pathlib import Path
from shutil import rmtree

REMOVE_PATHS = [
    "{%- if not cookiecutter.use_pytest -%}tests/{%- endif -%}",
]
REMOVE_PATHS = [Path(path_str) for path_str in REMOVE_PATHS if path_str]

for path in REMOVE_PATHS:
    if path and path.exists():
        rmtree(path)
