#!/usr/bin/python3
def number_of_lines(filename=""):
    counter = 0
    with open(filename) as f:
        for lines in f:
            counter = counter + 1
    return counter
