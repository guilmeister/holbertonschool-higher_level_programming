#!/usr/bin/python3
class Rectangle:
    """
    Class Rectangle that defines a rectangle:

    Args:
        width(int): width dimension of a rectangle
        height(int): height dimension of a rectangle
        number_of_instances(int): number of existing rectangles
        print_symbols(any): symbol to be printed
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances = Rectangle.number_of_instances + 1

    def __repr__(self):
        """Printable representational string of the given object"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Delete an item"""
        Rectangle.number_of_instances = Rectangle.number_of_instances - 1
        print("Bye rectangle...")

    def __str__(self):
        """String representation of object"""
        rectangle_print = ((Rectangle.print_symbol * self.__width + '\n') *
                           self.__height)
        return rectangle_print[:-1]

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares two rectangles and returns the bigger rectangle via area

        Args:
            rect_1: first rectangle with dimensions given
            rect_2: second rectangle with dimensions given
        """
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

    @classmethod
    def square(cls, size=0):
        """Class method that creates a square"""
        return cls(size, size)

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
        """Sets the height value if value is valid"""
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
