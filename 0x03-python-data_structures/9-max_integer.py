#!/usr/bin/python3
def max_integer(my_list=[]):
    limit = len(my_list)
    flag = 0
    if not my_list:
        return None
    else:
        for numbers in range(0, limit):
            flag = flag + 1
            if flag == 1:
                maximum = my_list[numbers]
                continue
            if my_list[numbers] > maximum:
                maximum = my_list[numbers]
        return maximum
