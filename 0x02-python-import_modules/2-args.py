#!/usr/bin/python3
import sys
argv = len(sys.argv) - 1
if __name__ == "__main__":
    print(argv, "arguments:")
    for i in range(argv):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
