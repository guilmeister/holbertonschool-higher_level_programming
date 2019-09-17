#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        for numbers in reversed(my_list):
            print("{:d}".format(numbers))
