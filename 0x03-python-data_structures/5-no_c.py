#!/usr/bin/env python3
def no_c(my_string):
    my_array = my_string.split()
    for char in my_array:
        if my_array[char] == 'c' or my_array[char] == 'C':
            my_string.remove[char]
