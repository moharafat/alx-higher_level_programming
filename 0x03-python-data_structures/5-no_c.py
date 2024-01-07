#!/usr/bin/env python3
def no_c(my_string):
    my_string = my_string.split()
    result = ""
    for char in my_string:
        if char.lower() != "c":
            result += char
    return result
