#!/usr/bin/python3
def save_to_json_file(my_obj, filename):
    """
    Function that writes an object to a text file using JSON
    """
    import json
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
