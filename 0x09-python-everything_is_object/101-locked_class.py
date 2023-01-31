#!/usr/bin/python3
"""
    This module containes a locked class that prevents the user
    from dynamilcally creating new instance attributes except if
    the attribute is first name
"""

class LockedClass:
    """ A locked class """

    __slots__ = ["first_name"]

    def __init__(self):
        """ Initializes self """

        pass
