#!/usr/bin/python3


def read_file(filename=""):
    """Read a text file"""
    with open(filename, mode="r", encoding="utf-8") as myfile:
        print(myfile.read(), end="")
