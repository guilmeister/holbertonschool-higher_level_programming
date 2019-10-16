#!/usr/bin/python3
class Student:
    """
    Class student
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializer
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Return dictionary representation
        """
        return self.__dict__
