#!/usr/bin/python3
def load_from_json_file(filename):
    """
    Function that creates an Object from a JSON file
    """
    import json
    with open(filename) as jsonf:
        data = json.load(jsonf)
        return data
