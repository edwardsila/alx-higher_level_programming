#!/usr/bin/python3

"""
module 0-read_file
opens a file in read mode

"""


def read_file(filename=""):
    """ opens a file """
    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
