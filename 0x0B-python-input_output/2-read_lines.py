#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    """
    Function that reads n lines of a file
    """
    counter = 0
    with open(filename) as f:
        for line in f:
            print(line, end="")
            counter = counter + 1
            if counter == nb_lines:
                break
