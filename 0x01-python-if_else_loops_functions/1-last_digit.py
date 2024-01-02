#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 0:
    dev = number % 10
    if dev > 5:
        print('Last digit of', number, 'is', dev, 'and is greater than 5')
    elif dev < 6:
        print('Last digit of', number, 'is', dev, 'and is less than 6 and not 0')	
elif number == 0:
    dev =(number %10)
    print('Last digit of', number, 'is', dev, 'and is 0')
elif number < 0:
    dev = number % -10
    if dev > 5:
        print('Last digit of', number, 'is', dev, 'and is greater than 5')
    elif dev < 6:
        print('Last digit of', number, 'is', dev, 'and is less than 6 and not 0')	
