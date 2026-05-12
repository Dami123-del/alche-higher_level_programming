#!/usr/bin/python3
"""
This module defines a Rectangle class that tracks the number of
active instances using a class attribute.
"""


class Rectangle:
    """
    A class that represents a rectangle.

    Attributes:
        number_of_instances (int): Tracks the number of active instances.
    """

    # Public class attribute
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes instance and increments the instance counter."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Retrieves the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the rectangle area."""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the rectangle perimeter."""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """Returns a string representation of the rectangle using #."""
        if self.__width == 0 or self.__height == 0:
            return ""
        rows = ["#" * self.__width for _ in range(self.__height)]
        return "\n".join(rows)

    def __repr__(self):
        """Returns a string to recreate the instance using eval()."""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Decrements the instance counter and prints a message upon deletion."""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
