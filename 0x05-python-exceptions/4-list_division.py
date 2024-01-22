#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    if not my_list_1 or not my_list_2:
        return []
    new_list = []
    for i in range(list_length):   
        try:
            new_list.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        #if len(my_list_1) != len(my_list_2):
        except IndexError:
            print("out of range")
    return new_list
