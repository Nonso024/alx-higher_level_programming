#!/usr/bin/python3
""" This module defines a txt file-reading function """


def read_file(filename=""):
    """ Prints the content of a UTF8 text file """
    
    with open(filename, emcoding="utf-8") as f:
        print(f.read(), end="")
