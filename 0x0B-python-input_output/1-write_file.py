#!/usr/bin/python3
""" This module contains a file-writing fuction """


def write_file(filename="", text=""):
    """ writes a string to a file in UTF8 encoding """

    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
