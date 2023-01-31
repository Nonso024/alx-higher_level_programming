#!/usr/bin/python3
"""
    This module contains a function add_integer(a,b)
    that adds two integers or floats and returns the sum
    a and b must be integers or floats else a 
    TypeError is raised
    If a or b is a float, it is first casted to an int so
    the function always returns an integer as the result
"""
def add_integer(a, b = 98):
    """ Adds 2 integers and retrns result """

    if type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")

    if type(a) == float:
        a = int(a)
    if type(b) == float:
        b =  int(b)

    return a + b
