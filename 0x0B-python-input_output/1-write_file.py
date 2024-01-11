#!/usr/bin/python3

"""
mod 1-write file
Function that writes a string to a text file (UTF8)
and returns the number of characters written.

"""


def write_file(filename="", text=""):
    """ Open the file in write mode with UTF-8 encoding """
    with open(filename, 'w', encoding="utf-8") as f:
        return f.write(text)
