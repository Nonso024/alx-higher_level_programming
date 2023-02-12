#!/usr/bin/python3
""" This module represents the base calss for other classes """



import csv
import json
import os
import turtle



class Base:
    """ Base class for other classese """

    __nb_objects = 0

    def __init__(self, id=None):
        """ """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
    
    @staticmethod
    def to_json_string(list_dictionaries):
        """ string representation of list of dictionaries """

        if not list_dictionaries:
            return json.dumps([])
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON representation of list_objs to a file """

        list_dict = []
        for obj in list_objs:
            obj_dict = obj.to_dictionary()
            list_dict.append(obj_dict)

        json_string = Base.to_json_string(list_dict)
        file_name = cls.__name__ + ".json"

        with open(file_name, "w") as f:
            f.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of a JSON representation json_string """

        if not json_string:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes set """

        dummy = cls(1, 1)
        dummy.update(**dictionary)

        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances loaded from a file """

        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, "r") as f:
                json_string = f.read()
        except FileNotFoundError:
            return []
        else:
            list_dict = Base.from_json_string(json_string)

        list_objs = []
        for obj_dict in list_dict:
            new_instance = cls.create(**obj_dict)
            list_objs.append(new_instance)

        return list_objs

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON representation of list_objs to a file """

        list_dict = []
        for obj in list_objs:
            obj_dict = obj.to_dictionary()
            list_dict.append(obj_dict)

        json_string = Base.to_json_string(list_dict)
        file_name = cls.__name__ + ".json"

        with open(file_name, "w") as f:
            f.write(json_string)
