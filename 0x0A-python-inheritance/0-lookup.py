#!/usr/bin/python3
""" 
    This module contains a function that returns a list of available 
    attributes and methods of an object
"""


def lookup(obj):
    """ returns list of attributes and methods """
    
    return (dir(obj))
