#!/usr/bin/python3
def print_list_integer(my_list=[]):
    limit = len(my_list)
    for numbers in range(0, limit):
        print("{:d}".format(my_list[numbers]))
