#!/usr/bin/python3
"""
Module 7-base_geometry
Defines a class BaseGeometry with area() and integer_validator() methods
"""


class BaseGeometry:
    """Empty class"""
    def area(self):
        """Raises an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Validates values"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
