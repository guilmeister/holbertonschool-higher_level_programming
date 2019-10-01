#!/usr/bin/python3
class Square:
    """Class Square"""
    def __init__(self, size=0):
        """Initializer"""
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
