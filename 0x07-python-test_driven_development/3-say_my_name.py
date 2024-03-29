#!/usr/bin/python3
"""

contains say_my_name function
writes the fist and second name if its ther
"""


def say_my_name(first_name, last_name=""):
    """
    writes the fist and second name if its ther
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
