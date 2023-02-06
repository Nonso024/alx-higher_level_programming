#!/usr/bin/python3
"""
    This module contains a class MyList that inherits from a list class.
    it has a method print_sorted(self)
"""


class MyList(self):
    """ Inherits from list class """

    def print_sorted(self):
        """ prints a sorted inherited list """

        sorted_list =  self.copy()
        sorted_list.sort()
        print(sorted_list)
