#!/usr/bin/python3
def max_integer(my_list=[]):
    # Check if the list is empty
    if not my_list:
        return None

    # Initialize the biggest integer with the first element
    biggest = my_list[0]

    # Iterate through the list
    for x in my_list:
        if x > biggest:
            biggest = x

    return biggest
