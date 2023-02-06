#!/usr/bin/python
"""
    This module contains a function that checks if an object is an instance
    of a class that inherited (directly/indirectly) from a specified class
"""


def inherits_from(obj, a_class):
    """ Checks if an object inherits from a class directly of indirectly """

    if type(obj) is not a_class:
        return True
    return (isinstance(obj, a_class))
