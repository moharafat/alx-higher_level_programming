#!/usr/bin/python3
"""
contains add_integer function
adds 2 integers or 1 integer to 98
"""
def add_integer(a, b=98):
    """
    adds 2 integers or 1 integer to 98
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
