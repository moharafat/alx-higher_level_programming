#!/usr/bin/python3
"""
Write a function that returns True
"""


def inherits_from(obj, a_class):
    """returns True if the object is exactly an insta/
    nce of the specified class"""
    if isinstance(obj, a_class):
        return (True)
    else:
        return False
