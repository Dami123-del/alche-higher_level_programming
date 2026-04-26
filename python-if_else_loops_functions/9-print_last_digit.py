#!/usr/bin/python3
def print_last_digit(number):
    # Get the absolute value to handle negative numbers
    if number < 0:
        number = -number

    last_digit = number % 10

    # Print the digit without a newline (using string format)
    print("{}".format(last_digit), end="")

    # Return the value as requested by the prototype
    return last_digit
