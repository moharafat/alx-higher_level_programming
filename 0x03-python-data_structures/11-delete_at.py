#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    new_list = []
    for idx in my_list:
        if idx == my_list[idx]:
            new_list.append(my_list[idx + 1])
    return new_list
