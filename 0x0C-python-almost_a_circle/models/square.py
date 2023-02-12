#!/usr/bin/python3
""" This module contains a representation of a square """

from models.rectangle import Rectangle


class Square(Rectangle):
    """ A class that represents a square """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initializes the attributes of a square """
        self.size = size
        self.x = x
        self.y = y
        self.id = None
        super()__init__(size, x, y, id)

    def __str__(self):
        """ Defines a format for string representation of the class """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"
    
    @property
    def size(self):
        """ Gets the value of size """
        return self.__width

    @size.setter
    """ sets size """
    def size(self, value):
        """ Sets the value for size """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")

        self.__width = value
        self.__height = value

    def update(self, *args, **kwargs):
        """ updates attributes of the instance """

        attrs = ["id", "size", "x", "y"]

        if not args:
            for key, value in kwargs.items():
                if key in attrs:
                    setattr(self, key, value)

        else:
            i = 0
            for val in args:
                setattr(self, attrs[i], value)
                i += 1
                if i > 3:
                    break

    def to_dictionary(self):
        """ returns the dictionary representation """

        attrs = ["id", "size", "x", "y"]
        dict_rep = {}

        for attr in attrs:
            val = getattr(self, attr)
            dict_rep[attr] = val

        return dict_rep
