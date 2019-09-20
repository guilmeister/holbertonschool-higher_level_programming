#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionary = a_dictionary.copy()
    for x in new_dictionary:
        double = new_dictionary[x] * 2
        new_dictionary.update({x: double})
    return new_dictionary
