#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None or my_list is []:
        return None
    new_list = my_list.copy()
    for numbers in new_list:
        if numbers % 2 == 0:
            new_list[numbers] = True
        else:
            new_list[numbers] = False
    return new_list
