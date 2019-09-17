#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    limit = len(my_list)
    if idx < 0 or idx > limit:
        return my_list
    else:
        my_list[idx] = element
        return my_list
