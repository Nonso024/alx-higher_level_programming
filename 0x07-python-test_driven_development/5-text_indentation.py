#!/usr/bin/python3
"""
    This module contains a function text_indentation(text)
    that prints a text wiyh 2 newline characters
    text must be atring else raise TypeError
"""

def text_indentation(text):
    """ Prints a text and 2 newlines after any of the
        characters . ? or :
    """

    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in range(len(text)):
        print(text[i], end="")
        if text[i] in [".", "?", ":"]:
            print()
            print()
            if i != len(text) - 1 and text[i + 1] == " ":
                i += 1
