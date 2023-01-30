#!/usr/bin/python3
""" A module that defines a square """

class Square:
    """ A class that represnts a square """

    def __init__(self, size=0):
        """ Initializing self """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size