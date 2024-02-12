#!/usr/bin/python3
"""Defining a class [Base]."""
import json


class Base:
    """Representing the base model"""


    __nb_objects = 0

    def __init__(self, id=None):
        """Initilizing the base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returs a JSON serliئation"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the deserlization of a JSON  string"""
        if json_string is None or len(json_string) == 0:
            return "[]"
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if (dictionary) and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new_class = cls(1,1)
            else:# Square case
                new_class = cls(1)
            new_class.update(**dictionary)
            return new_class
