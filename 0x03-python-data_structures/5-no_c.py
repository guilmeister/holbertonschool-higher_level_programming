#!/usr/bin/python3
def no_c(my_string):
    result = ''
    for character in my_string:
        if character in "cC":
            result = result + ''
        else:
            result = result + character
    return result
