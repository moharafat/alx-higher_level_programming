#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_values = set()
    if len(my_list) == 0:
        return 0
    for number in (my_list):
        if number not in unique_values:
            unique_values.add(number)
        addition = sum(unique_values)
    return addition
