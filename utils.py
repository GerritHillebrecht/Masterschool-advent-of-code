import json


def save_to_file(data: list[int], file_name: str):
    with open(file_name, "w") as handle:
        handle.write(json.dumps(data))


def read_from_file(file_name: str) -> list[int]:
    with open(file_name, "r") as handle:
        return json.loads(handle.read())
