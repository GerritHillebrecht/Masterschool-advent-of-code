import json
from os.path import join

from config import dirname_storage_files


def save_to_file(data: list[int], file_name: str):
    with open(join(dirname_storage_files, file_name), "w") as handle:
        handle.write(json.dumps(data))


def read_from_file(file_name: str) -> list[int]:
    with open(join(dirname_storage_files, file_name), "r") as handle:
        return json.loads(handle.read())
