#!/usr/bin/python3
def uppercase(str):
	for char in str:
		if 'a' <= char <= 'z':
			cap = chr(ord(char) - 32)
			print(cap, end="")
		else:
			print(char, end="")
