#!/usr/bin/python3
import hidden_4
list = dir(hidden_4)
if __name__ == "__main__":
    for i in list:
        if not i.startswith("__"):
            print(f"{i}")
