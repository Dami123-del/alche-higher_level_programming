#!/usr/bin/python3
"""This module defines the BaseGeometry class.

It provides a blueprint for geometric shapes, offering structural validation
utilities for dimensions like width and height.
"""


class BaseGeometry:
    """A base class for geometric operations."""

    def area(self):
        """Calculate the area of the geometry.

        Raises:
            Exception: Always, because subclasses must implement this.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that a given value is a positive integer.

        Args:
            name (str): The descriptive name of the value (e.g., "width").
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
