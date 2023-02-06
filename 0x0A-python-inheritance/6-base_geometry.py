#!/usr/bin/python3
"""
    This module conatains a class BaseGeometry and a public instance method
    area() that raises an exception
"""


class BaseGeometry:
    """ Class that contains public instance method area() """

    def area(self):
        """ method that raises an exception """

        raise Exception("area() is not implemented")
