#!/usr/bin/python3
def read_file(filename=""):
    """
    Function that reads and prints text from a file
    """
    with open(filename) as f:
        data = f.read()
        print(data, end="")
