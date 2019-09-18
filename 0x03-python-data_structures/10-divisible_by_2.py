#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list is None or my_list is []:
        return None
    new_list = []
    for numbers in my_list:
        if numbers % 2 == 0:
            new_list.append(True)
        else:
            new_list.append(False)
    return new_list
