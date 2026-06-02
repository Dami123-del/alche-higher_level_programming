#!/usr/bin/python3
"""This module provides a utility function for object type validation.

It checks whether an object is an instance of, or inherited from, a class.
"""


def is_kind_of_class(obj, a_class):
    """Check if an object is an instance or an inherited instance of a class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if obj is an instance of a_class or a subclass of it;
              otherwise False.
    """
    return isinstance(obj, a_class)
