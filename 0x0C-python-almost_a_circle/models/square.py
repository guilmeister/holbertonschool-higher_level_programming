#!/usr/bin/python3
from models.rectangle import Rectangle

class Square(Rectangle):

    def __init__(self, size, x=0, y=0, id=None):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size <= 0:
            raise ValueError("size must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        super().__init__(size, size, x, y, id)
        self.__size = size

    def __str__(self):
        sqr_prt = "[Square] ({}) {}/{} - {}".format(self.id,
                                                    self.x,
                                                    self.y,
                                                    self.size)
        return sqr_prt

    def to_dictionary(self):
        sqr_dict = {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
        return sqr_dict

    def update(self, *args, **kwargs):
        update_list = []
        limit = len(args)
        if args is not None:
            for arg in args:
                update_list.append(arg)
            if limit >= 4:
                self.id = update_list[0]
                self.size = update_list[1]
                self.x = update_list[2]
                self.y = update_list[3]
            elif limit == 3:
                self.id = update_list[0]
                self.size = update_list[1]
                self.x = update_list[2]
            elif limit == 2:
                self.id = update_list[0]
                self.size = update_list[1]
            elif limit == 1:
                self.id = update_list[0]
        if kwargs is not None:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.width = value
#        if type(value) is not int:
#            raise TypeError("size must be an integer")
#        if value <= 0:
#            raise ValueError("size must be > 0")
        self.__size = value
