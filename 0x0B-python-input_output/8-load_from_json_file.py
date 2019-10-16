#!/usr/bin/python3
def load_from_json_file(filename):
    import json
    with open(filename) as jsonf:
        data = json.load(jsonf)
        return data
