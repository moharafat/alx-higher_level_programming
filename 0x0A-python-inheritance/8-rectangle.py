#!/usr/bin/python3
"""
Defining a class Rctangle inherited from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator(self, width)
        self.__width = width