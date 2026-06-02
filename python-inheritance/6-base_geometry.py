#!/usr/bin/python3
"""This module defines the BaseGeometry class.

It serves as the base layer foundation for future geometry-related
class extensions and calculations.
"""


class BaseGeometry:
    """A base class for geometric operations."""

    def area(self):
        """Calculate the area of the geometry.

        Raises:
            Exception: Always raises an Exception since the method
                       is intended to be implemented by subclasses.
        """
        raise Exception("area() is not implemented")
