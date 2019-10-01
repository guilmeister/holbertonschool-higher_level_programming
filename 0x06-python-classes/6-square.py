#!/usr/bin/python3
class Square:
    """Class Square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initializer"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter for size"""
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Getter for position"""
        return self.__position

    @position.setter
    def position(self, value):
        """Getter for position"""
        if isinstance(value, tuple) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[0], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        if isinstance(value[1], int) is False:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Printing box"""
        if self.__size == 0:
            print("")
            return
        for x in range(0, self.__position[1]):
            print("")
        for x in range(0, self.__size):
            for z in range(0, self.__position[0]):
                print(" ", end="")
            for y in range(0, self.__size):
                print("#", end="")
            print("")

    def area(self):
        """Returning size"""
        return self.__size
