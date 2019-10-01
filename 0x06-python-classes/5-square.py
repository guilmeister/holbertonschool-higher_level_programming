#!/usr/bin/python3
class Square:
    """Class Square"""
    def __init__(self, size=0):
        """Initializer"""
        self.__size = size

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

    def my_print(self):
        """Square Printer"""
        if self.__size == 0:
            print("")
        for x in range(0, self.__size):
            for y in range(0, self.__size):
                print("#", end="")
            print("")

    def area(self):
        """Return size"""
        return self.__size
