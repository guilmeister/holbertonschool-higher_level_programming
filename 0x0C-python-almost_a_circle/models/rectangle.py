#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    def to_dictionary(self):
        dict_form = {'id': self.id,
                     'width': self.__width,
                     'height': self.__height,
                     'x': self.__x,
                     'y': self.__y}
        return dict_form

    def update(self, *args, **kwargs):
        update_list = []
        limit = len(args)
        if args is not None:
            for arg in args:
                update_list.append(arg)
            if limit >= 5:
                self.id = update_list[0]
                self.__width = update_list[1]
                self.__height = update_list[2]
                self.__x = update_list[3]
                self.__y = update_list[4]
            elif limit == 4:
                self.id = update_list[0]
                self.__width = update_list[1]
                self.__height = update_list[2]
                self.__x = update_list[3]
            elif limit == 3:
                self.id = update_list[0]
                self.__width = update_list[1]
                self.__height = update_list[2]
            elif limit == 2:
                self.id = update_list[0]
                self.__width = update_list[1]
            elif limit == 1:
                self.id = update_list[0]
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.__width = value
                if key == "height":
                    self.__height = value
                if key == "x":
                    self.__x = value
                if key == "y":
                    self.__y = value

    def __str__(self):
        rec_prt = "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                          self.__x,
                                                          self.__y,
                                                          self.__width,
                                                          self.__height)
        return rec_prt

    def area(self):
        return self.__width * self.__height

    def display(self):
        for space_hor in range(self.__y):
            print("")
        for horizontal in range(self.__height):
            for space_ver in range(self.__x):
                print(" ", end="")
            for vertical in range(self.__width):
                print("#", end="")
            print("")

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
