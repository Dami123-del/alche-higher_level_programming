#!/usr/bin/python3
def uppercase(str):
    for char in str:
        # Check if the character is lowercase
        if ord(char) >= 97 and ord(char) <= 122:
            # Shift the value by -32 to get the uppercase equivalent
            char = chr(ord(char) - 32)

        print("{}".format(char), end="")

    # Print the required new line
    print("")
