#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Create a copy of the original list
    copy_list = my_list[:]

    # Check if idx is negative or out of range
    if idx < 0 or idx >= len(my_list):
        return copy_list

    # Replace the element in the copy
    copy_list[idx] = element

    return copy_list
