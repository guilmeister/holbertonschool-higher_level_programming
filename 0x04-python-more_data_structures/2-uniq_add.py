#!/usr/bin/python3
def uniq_add(my_list=[]):
    if my_list:
        unique_list = []
        for element in my_list:
            if element not in unique_list:
                unique_list.append(element)
        return sum(unique_list)
