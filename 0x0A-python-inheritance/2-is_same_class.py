#!/usr/bin/python3
"""
is_same_class function usese the
type function to determine type of
object and compares it with the specified
class using the is operator

"""


def is_same_class(obj, a_class):

    """ Check if obj is exactly instance of class """

    return type(obj) is a_class
