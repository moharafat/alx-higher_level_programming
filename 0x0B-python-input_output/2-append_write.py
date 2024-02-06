#!/usr/bin/python3
"""Defining a file-writing function."""


def append_write(filename="", text=""):
    """append a string to a UTF8 text file.
    Arguments:
        filename: The name of the file to append.
        text : The text to append to the file.
    Returns: The number of characters appendedd.
    """
    with open(filename, mode="a", encoding="utf-8") as myFIle:
        return myFIle.write(text)
