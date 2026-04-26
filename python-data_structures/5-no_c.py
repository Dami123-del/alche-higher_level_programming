#!/usr/bin/python3
def no_c(my_string):
    # Initialize an empty string to store the result
    new_string = ""

    # Iterate through each character in the input string
    for char in my_string:
        # Check if the character is NOT 'c' and NOT 'C'
        if char != 'c' and char != 'C':
            new_string += char

    return new_string
