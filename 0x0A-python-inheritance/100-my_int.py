#!/usr/bin/python3
"""
    This module contains a class MyInt that inherits from the int class
    MyInt has == and != inverted
"""


class MyInt(int):
    """ MyInt class inherited from the class int """

    def __eq__(self, obj):
        """ Calls for equal-to comparison """

        return super().__ne__(obj)

    def __ne__(self, obj):
        """ Calls for not qual-to comaprison """

        return super().__eq__(obj)
