#!/usr/bin/python3
"""
Write a function that returns True
"""


def is_same_class(obj, a_class):
    """returns True if the object is exactly an instance of the specified class"""
    if type(obj) == a_class:
        return (True)
    else:
        return False
