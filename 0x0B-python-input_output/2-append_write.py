#!/usr/bin/python3

"""
mod 2-appendwrite
appenda a string at the end
of a text

"""


def append_write(filename="", text=""):
    """ function appenda a string at end of a text """
    with open(filename='', 'a', encoding="utf-8") as f:
        return f.write(text)
