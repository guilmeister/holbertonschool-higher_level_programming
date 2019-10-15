#!/usr/bin/python3
class BaseGeometry:
    """
    Empty class BaseGeometry
    """
    pass

    def area(self):
        """
        Function that prints the area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Function that validates inputs
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    Class Rectangle
    """

    def __init__(self, width, height):
        """
        Validate inputes before initializing values
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        String representation of an object
        """
        rectangle_print = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return rectangle_print

    def area(self):
        """
        Returns value of area
        """
        return self.__width * self.__height

class Square(Rectangle):
    """
    Class Square
    """

    def __init__(self, size):
        """
        Validate inputs before initializing values
        """
        BaseGeometry.integer_validator(self, "square", size)
        self.__size = size

    def __str__(self):
        """
        String representation of an object
        """
        rectangle_print = "[Rectangle] {}/{}".format(self.__size, self.__size)
        return rectangle_print

    def area(self):
        """
        Returns value of area
        """
        return self.__size * self.__size
