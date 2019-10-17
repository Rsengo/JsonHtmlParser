import json


def deserialize(path):
    with open(path, "r") as read_file:
        return json.load(read_file)
