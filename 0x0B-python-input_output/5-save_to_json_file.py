#!/usr/bin/python3
"""Defining a file-writing function."""
import json


def save_to_json_file(my_obj, filename):
    """
    Returns:  JSON representation of an object (stringz).
    """
    with open(filename, "w") as file:
        json.dump(my_obj, file)
