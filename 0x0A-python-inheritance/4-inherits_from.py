#!/usr/bin/python3
"""
Module 4-inherits_from
Checks if an object is an instance inherited (directly or indirectly)
from a specific class

"""


def inherits_from(obj, a_class):
    """Returns True if obj is an instance inherited from a_class"""
    return issubclass(type(obj), a_class) and type(obj) != a_class