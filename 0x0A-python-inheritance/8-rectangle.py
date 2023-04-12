#!/usr/bin/python3
"""Defines a Rectangle class that inherits from BaseGeometry class."""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an Exception with an explanation message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a given value if it is a positive integer

        Args:
            name (str): the name string
            value (int): the value to validate

        Raises:
            TypeError: if `value` is not an integer
            ValueError: if `value` is less or equal to 0
        """
        if type(value) is not int:
            raise TypeError(name + " must be an integer")
        if value <= 0:
            raise ValueError(name + " must be greater than 0")


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """Instantiates a Rectangle object with given width and height"""
        self.__width = width
        self.__height = height
        super().integer_validator("width", width)
        super().integer_validator("height", height)
