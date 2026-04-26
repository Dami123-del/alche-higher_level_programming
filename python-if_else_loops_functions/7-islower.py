#!/usr/bin/python3
def islower(c):
    """
    Checks if a character is lowercase using its Unicode code point.
    """
    # Check if the character's ord value is between 'a' and 'z'
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False
