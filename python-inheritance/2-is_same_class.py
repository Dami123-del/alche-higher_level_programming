#!/bin/usr/python3
"""This module defines the MyList class.

It provides extended functionality over the standard built-in list.
"""


class MyList(list):
    """A custom list class that inherits from the built-in list."""

    def print_sorted(self):
        """Print the elements of the list sorted in ascending order.

        Assumes all elements in the list are of a comparable type
        (e.g., integers).
        """
        sorted_list = sorted(self)
        print(sorted_list)
