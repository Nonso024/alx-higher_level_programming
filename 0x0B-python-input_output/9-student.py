#!/usr/bin/python3
""" A class representing Students info """


class Student:
    """ represents a student """

    def __init__(self, first_name, last_name, age):
        """ Initializing a new student """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Gets a dictionary rep of the Student class """
        return self.__dict__
