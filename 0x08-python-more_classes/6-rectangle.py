#!/usr/bin/python3
class Rectangle:
    """
    Class Rectangle that defines a rectangle:

    Args:
        width(int): width dimension of a rectangle
        height(int): height dimension of a rectangle
        number_of_instances(int): number of existing rectangles
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    def __repr__(self):
        """Printable representational string of the given object"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an item"""
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print("Bye rectangle...")

    def __str__(self):
        """String representation of object"""
        rectangle_print = (('#' * self.__width + '\n') * self.__height)
        return rectangle_print[:(self.__height * self.__width) +
                                (self.__height - 1)]

    @property
    def width(self):
        """Returns width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets width value if value is valid"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns height value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets height value if value is valid"""
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area value of the dimensions of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """Returns the perimeter value of the dimensions of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))
