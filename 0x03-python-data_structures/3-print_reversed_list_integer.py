#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    limit = len(my_list) - 1
    for numbers in range(limit, -1, -1):
        print("{}".format(my_list[numbers]))
