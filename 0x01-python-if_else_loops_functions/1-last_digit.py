#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number > 5:
		dev =(number %10)
		print('last digit of', number, 'is', dev, 'and is greater than 5')
elif number == 0:
	dev =(number %10)
	print('last digit of', number, 'is', dev, 'and is 0')
elif number < 6:
	dev = -(number %10)
	print('last digit of', number, 'is', dev)