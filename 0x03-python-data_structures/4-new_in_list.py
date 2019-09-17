#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    limit = len(my_list)
    new_list = list(my_list)
    if idx < 0 or idx > limit:
        return my_list
    else:
        new_list[idx] = element
        return new_list
