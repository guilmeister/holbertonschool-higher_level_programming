#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for y in range(0, x):
            print("{:d}".format(my_list[y]), end="")
        print("")
        return(y + 1)
    except IndexError:
        print("")
        return(y)
