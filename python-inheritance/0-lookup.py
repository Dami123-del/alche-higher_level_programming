#!/usr/bin/python3
"""This module provides utility functions for object inspection.

It contains functions designed to look up and list the attributes
and methods available on any given Python object.
"""


def lookup(obj):
    """Return a list of available attributes and methods of an object.

    Args:
        obj: The object to inspect.

    Returns:
        list: A list of strings representing the object's attributes
        and methods.
    """
    return dir(obj)
