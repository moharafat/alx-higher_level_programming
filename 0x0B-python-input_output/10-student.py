#!/usr/bin/python3
"""Defining a file-writing function."""


class Student:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Returns:retrieves a dictionary representation of a Student
        """
        if attrs
        return self.__dict__
