#!/usr/bin/python3

x = int(input("please enter integer"))
if x < 0:
    x = 0
    print('-ve to zero')
elif x == 0:
    print('zero')
elif x == 1:
    print('Single')

else:
    print('more')