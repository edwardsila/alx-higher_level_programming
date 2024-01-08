#!/usr/bin/python3

"""
This class MyList
inherits from list and
prints list in sorted form

"""


class MyList(list):

    """ inherits from list """

    def print_sorted(self):

        """ prints list in ascending order """

        sorted_list = sorted(self)
        print(sorted_list)
