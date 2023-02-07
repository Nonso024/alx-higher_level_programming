#!/usr/bin/python3
""" This module contains a file-writing function that appends a string """


def append_write(filename="", text=""):
    """ Appends a string to a file with UTF8 encoding """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
