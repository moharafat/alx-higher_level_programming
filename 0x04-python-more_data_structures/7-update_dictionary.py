#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    sorted_keys = sorted(a_dictionary)
    for key in sorted_keys:
        value = a_dictionary[key]
        print(f"{key}: {value}")
