#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    length = 0
    actual = 0
    for i in my_list:
        if(isinstance(i, int)):
            length = length + 1
    try:
        for y in range(0, x):
            if(isinstance(my_list[y], int)):
                actual = actual + 1
                print("{:d}".format(my_list[y]), end="")
        print("")
        return(actual)
    except (TypeError, ValueError):
        print("")
        return(actual)
