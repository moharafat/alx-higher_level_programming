#!/usr/bin/python3
"""Defining a file-writing function."""


def class_to_json(obj):
    """
    Returns:  JSON representation of an object (stringz).
    """
    return obj.__dict__
