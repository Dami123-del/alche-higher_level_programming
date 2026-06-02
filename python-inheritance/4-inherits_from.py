#!/usr/bin/python3
"""This module provides a utility function for inheritance validation.

It checks whether an object inherits from a specified class directly
or indirectly, excluding direct instances of the class itself.
"""


def inherits_from(obj, a_class):
    """Check if an object is an instance of a class that inherited from a_class.

    Args:
        obj: The object to check.
        a_class: The class to check against.

    Returns:
        bool: True if obj's class is a subclass of a_class (but not a_class itself);
              otherwise False.
    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
