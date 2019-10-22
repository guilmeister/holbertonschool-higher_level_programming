#!/usr/bin/python3

"""
This is a Base Module for Base Class
"""

import json
from os import path


class Base:
    """
    Class Base
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Function that initializes
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method that returns JSON string representation
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method that writes JSON string representation to a file
        """
        new_list = []
        if list_objs is None:
            pass
        else:
            for elements in list_objs:
                new_list.append(elements.to_dictionary())
        with open("{}.json".format(cls.__name__), "w") as f:
            f.write(cls.to_json_string(new_list))

    @classmethod
    def load_from_file(cls):
        """
        Class method that returns list of instances
        """
        files = cls.__name__ + '.json'
        file_exists = path.isfile(files)
        new_list = []
        if file_exists:
            with open("{}.json".format(cls.__name__), "r") as f:
                data = json.load(f)
            for values in data:
                new_list.append(cls.create(**values))
        return new_list

    @staticmethod
    def from_json_string(json_string):
        """
        Static method that returns list of JSON string representation
        """
        if json_string is None:
            return
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Class method that returns instance with all attributes set
        """
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(5, 5)
        elif cls.__name__ == "Square":
            dummy_instance = cls(5)
        dummy_instance.update(**dictionary)
        return dummy_instance
