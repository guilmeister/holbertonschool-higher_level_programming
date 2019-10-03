#!/usr/bin/python3
def print_square(size):
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    elif isinstance(size, int) is False:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for x in range(0, size):
        for y in range(0, size):
            print("#", end="")
        print("")
