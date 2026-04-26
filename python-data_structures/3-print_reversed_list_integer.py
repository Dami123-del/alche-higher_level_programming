#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    # Iterate through the list in reverse using slicing [::-1]
    for i in my_list[::-1]:
        print("{:d}".format(i))
