#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
dev =(number %10)
print('last digit of', number, 'is', dev)