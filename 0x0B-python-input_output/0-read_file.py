#!/usr/bin/python3


def read_file(filename=""):
    """prints the conent of a file[utf-8] to stdout"""
    with open(filename, mode="r", encoding="utf-8") as f
        print(f.read(), end="")
