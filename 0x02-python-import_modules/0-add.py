#!/usr/bin/python3

from add_0 import add

a = 1
b = 2
sum = add(a, b)
#only works if we are executing from main file
if __name__ == "__main__":
    print("{0} + {1} = {2}".format(a, b, sum))
