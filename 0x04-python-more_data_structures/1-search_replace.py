#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for x, to_replace in enumerate(new_list):
        if to_replace == search:
            new_list[x] = replace
    return new_list
