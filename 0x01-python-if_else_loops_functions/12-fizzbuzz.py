#!/usr/bin/python3
def fizzbuzz():
    for mult in range(1, 101):
        if mult % 3 == 0 and mult % 5 == 0:
            print("FizzBuzz", end=" ")
        elif mult % 3 == 0:
            print("Fizz", end=" ")
        elif mult % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{:d}".format(mult), end=" ")
