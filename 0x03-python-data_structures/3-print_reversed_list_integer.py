#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    limit = len(my_list)
    for numbers in range(limit - 1, 0 - 1, -1):
        print("{}".format(my_list[numbers]))
