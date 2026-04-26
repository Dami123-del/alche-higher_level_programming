#!/usr/bin/python3
def multiple_returns(sentence):
    # Calculate the length of the string
    length = len(sentence)

    # Determine the first character
    if length == 0:
        first_char = None
    else:
        first_char = sentence[0]

    # Return both values as a tuple
    return (length, first_char)
