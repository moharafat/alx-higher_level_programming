#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None
    max_integer = my_list[0]
    for number in my_list:
        if number >= max_integer:
           max_integer = number
    return max_integer