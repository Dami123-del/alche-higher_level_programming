#!/usr/bin/python3
def fizzbuzz():
    for i in range(1, 101):
        # Check if divisible by both 3 and 5
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=" ")
        # Check if divisible by 3
        elif i % 3 == 0:
            print("Fizz", end=" ")
        # Check if divisible by 5
        elif i % 5 == 0:
            print("Buzz", end=" ")
        # Otherwise, print the number
        else:
            print("{}".format(i), end=" ")
