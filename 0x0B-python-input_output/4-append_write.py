#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    Function that appends a string at the end a text file
    """
    with open(filename, "a") as f:
        return f.write(text)
