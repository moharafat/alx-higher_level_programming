#!/usr/bin/python3
"""
 raises an Exception with the message area() is not implemented
"""


class BaseGeometry:
    """class BaseGeomtry"""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
