#!/usr/bin/python3
"""

contains text_indentation function
new line at signal
"""


def text_indentation(text):
    """
    new line at signal
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for i in text:
        if i in ['.', '?', ':']:
            print(i, end="")
            print("\n")
        else:
            print(i, end="")
