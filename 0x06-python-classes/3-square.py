#!/usr/bin/python3
""" A module that defines a square """

class Square:
    """ This class represents a square class with a private 
    attribut instance """

    def __init__(self, size=0):
        """ Initializes self """

        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        id size < 0:
            raise ValueError('size must be >= 0')

        self.__size = size

    def area(self):
        """ Returns the area of the sqaure """

        return self.__size * self.__size
