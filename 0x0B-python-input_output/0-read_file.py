#!/usr/bin/python3
"""read file module"""


def read_file(filename=""):
    """Read a text file"""
    with open(filename, mode="r", encoding="utf-8") as myfile:
        print(myfile.read(), end="")
