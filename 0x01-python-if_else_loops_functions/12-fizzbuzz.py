#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 5 == 0 and number % 3 == 0:
            print("FizzBuzz ", end="")
            continue
        if number % 5 == 0:
            print("Buzz ", end="")
            continue
        if number % 3 == 0:
            print("Fizz ", end="")
            continue
        print(number, "", end="")
