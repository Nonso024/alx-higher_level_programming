#!/usr/bin/python3
"""
    This module contains a function that checks for similarity between
    object and specified class. It returns true if object is an exact
    instance and returns false if otherwise
"""


def is_same_class(obj, a_class):
    """ checks for similarity in instance """

    if type(obj) == a_class:
        return True
    else:
        return False
