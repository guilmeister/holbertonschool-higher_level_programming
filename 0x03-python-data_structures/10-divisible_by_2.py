#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = list(my_list)
    for numbers in new_list:
        if numbers % 2 == 0:
            new_list[numbers] = True
        else:
            new_list[numbers] = False
    return new_list
