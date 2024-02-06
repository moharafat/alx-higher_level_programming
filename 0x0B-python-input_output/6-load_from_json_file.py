#!/usr/bin/python3
"""Defining a file-writing function."""
import json


def load_from_json_file(filename):
    """
    Returns:  JSON representation of an object (stringz).
    """
    with open(filename, "r") as file:
        return json.load(file)
