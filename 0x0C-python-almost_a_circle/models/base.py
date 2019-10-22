#!/usr/bin/python3
import json


class Base:

    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
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
        new_list = []
        with open("{}.json".format(cls.__name__), "r") as f:
            data = json.load(f)
        for values in data:
            new_list.append(cls.create(**values))
        return new_list

    @staticmethod
    def from_json_string(json_string):
        if json_string is None:
            return
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy_instance = cls(5, 5)
        elif cls.__name__ == "Square":
            dummy_instance = cls(5)
        dummy_instance.update(**dictionary)
        return dummy_instance
