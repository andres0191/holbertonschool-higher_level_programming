#!/usr/bin/python3
import json


class Base:
    """ The first class for the project almost a circle"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            list_dictionaries = []
            return list_dictionaries
        else:
            return (json.dumps(list_dictionaries))
