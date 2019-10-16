#!/usr/bin/python3
def from_json_string(my_str):
    """
    Function that returns an object represented by JSON string
    """
    import json
    return json.loads(my_str)
