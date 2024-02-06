#!/usr/bin/python3
"""Defining a file-writing function."""
import json


def from_json_string(my_str):
    """
    Returns:  JSON representation of an object (stringz).
    """
    return json.dumps(my_str)
