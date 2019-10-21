#!/usr/bin/python3
class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
#            Base.__nb_objects = Base.__nb_objects + 1
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
