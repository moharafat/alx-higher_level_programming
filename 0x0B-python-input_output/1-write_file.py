#!/usr/bin/python3
"""Defining a file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.
    Arguments:
        filename: The name of the file to write.
        text : The text to write to the file.
    Returns: The number of characters written.
    """
    with open(filename, mode="w", encoding="utf-8") as myFIle:
        return myFIle.write(text)
