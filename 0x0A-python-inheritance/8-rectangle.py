#!/usr/bin/python
"""
    This module contains a class Rectangle that inherits from a class
    BaseGeometry
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """ A rectangle that is a subclass of the BaseGeometry class """

    def __init__(self, width, height):
        """ Initializes self """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
