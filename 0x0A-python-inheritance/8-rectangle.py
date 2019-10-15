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

    def __init__(self, width, height):
        """
        Validate inputes before initializing values
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
