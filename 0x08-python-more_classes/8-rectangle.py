#!/usr/bin/python3
class Rectangle:

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    def __del__(self):
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print("Bye rectangle...")

    def __str__(self):
        rectangle_print = ((Rectangle.print_symbol * self.__width + '\n') * self.__height)
        return rectangle_print[:(self.__height * self.__width) +
                                (self.__height - 1)]
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if isinstance(rect_1, Rectangle) is False:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if isinstance(rect_2, Rectangle) is False:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        if rect_1.area() < rect_2.area():
            return rect_2
        if rect_1.area() == rect_2.area():
            return rect_1

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if isinstance(value, int) is False:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__height = value

    def area(self):
        return self.__height * self.__width

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))
