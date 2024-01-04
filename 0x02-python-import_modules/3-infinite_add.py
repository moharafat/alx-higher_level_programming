#!/usr/bin/python3
import sys
if __name__ == "__main__":
    argv = len(sys.argv) - 1
    sum = 0
    for i in range(argv):
        sum = sum + int(sys.argv[i + 1])
    print(f"{sum}")
