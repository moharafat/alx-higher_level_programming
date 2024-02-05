#!/usr/bin/python3
"""
 raises an Exception with the message area() is not implemented
"""


class BaseGeometry:
    """class BaseGeomtry"""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
