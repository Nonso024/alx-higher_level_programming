#!/usr/bin/python3
""" A module that defines a JSON-to-object function """


import json


def from_json_string(my_str):
    """ Returns the python object rep of a JSON string """
    return json.loads(my_str)
