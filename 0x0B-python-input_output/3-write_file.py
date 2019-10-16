#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Function that writes given string to a file
    """
    with open(filename, "w") as f:
        return f.write(text)
