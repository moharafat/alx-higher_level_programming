#!/usr/bin/python3
def print_last_digit(number):
    if number > 0:
        dev = number % 10
        print(dev, end="")
        return dev
    elif number < 0:
        dev = number % -10
        print(abs(dev), end="")
        return abs(dev)
    else:
        dev = 0
        print(dev, end="")
        return dev
