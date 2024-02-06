#!/usr/bin/python3
"""Defining a file-writing function."""
import json


def to_json_string(my_obj):
    """
    Returns:  JSON representation of an object (stringz).
    """
    return json.dumps(my_obj)
