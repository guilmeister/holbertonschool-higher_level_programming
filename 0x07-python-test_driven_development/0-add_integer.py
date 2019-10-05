#!/usr/bin/python3
"""Module to find the sum of two integers



"""


def add_integer(a, b=98):
    """Function that adds two integers

    """
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    if isinstance(a, int) is False:
        raise TypeError("a must be an integer")
    if isinstance(b, int) is False:
        raise TypeError("b must be an integer")
    return a + b
