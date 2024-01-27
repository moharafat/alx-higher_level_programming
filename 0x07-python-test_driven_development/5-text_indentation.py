#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    for i in text:
        if i in ['.', '?', ':']:
            print(i, end="")
            print("\n")
        else:
            print(i, end="")
