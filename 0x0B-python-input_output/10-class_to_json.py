#!/usr/bin/python3
def class_to_json(obj):
    """
    Returns dictionary of a class
    """
    return obj.__dict__
