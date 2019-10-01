#!/usr/bin/python3
class Square:
    """Class Square"""
    def __init__(self, size=0):
        """Initializer"""
        self.size = size

    @property
    def size(self):
        """Retriever"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter"""
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return Area"""
        return self.__size * self.__size
