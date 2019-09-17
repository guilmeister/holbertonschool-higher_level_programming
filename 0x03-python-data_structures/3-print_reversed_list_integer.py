#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    limit = len(my_list)
    if my_list:
        for numbers in reversed(range(0, limit)):
            print("{:d}".format(my_list[numbers]))
