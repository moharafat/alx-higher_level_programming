#!/usr/bin/python3
def print_square(size):
     if not isinstance(size, int):
        raise TypeError("size must be an integer")