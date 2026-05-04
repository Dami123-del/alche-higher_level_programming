#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # Get the keys, sort them alphabetically, and print key-value pairs
    for key in sorted(a_dictionary.keys()):
        print(f"{key}: {a_dictionary[key]}")
