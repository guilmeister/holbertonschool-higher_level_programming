#!/usr/bin/python3
def element_at(my_list, idx):
    limit = len(my_list)
    if idx < 0 or idx >= limit:
        return None
    else:
        return my_list[idx]
