#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    for i in my_list:
        length = length + 1
    try:
        for y in range(0, x):
            print("{}".format(my_list[y]), end="")
        print("")
        return(y + 1)
    except:
        print("")
        return(y)
