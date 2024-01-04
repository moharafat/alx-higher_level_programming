#!/usr/bin/python3
import sys
argv = len(sys.argv) - 1
if __name__ == "__main__":
    if argv == 0:
        print("0 arguments.")
    elif argv == 1:
        print("1 argument:")
        print("1: {}".format(sys.argv[1]))
    else:
        print(argv, "arguments:")
        for i in range(argv):
            print("{}: {}".format(i + 1, sys.argv[i + 1]))
