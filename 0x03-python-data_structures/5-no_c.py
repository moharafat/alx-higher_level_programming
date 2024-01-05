#!/usr/bin/env python3
def no_c(my_string):
    my_array = my_string.split()
    for i in my_array:
        if my_array[i] == 'c' or my_array[i] == 'C':
            del my_string[i]
