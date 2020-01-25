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

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            empty_file = []
            empty_file = cls.__name__
            with open(empty_file, 'w') as file:
                file.read([])
        else:
            new_list = []
            for i in range(len(list_objs)):
                new_doc = list_objs[i].__class__.__name__
                new_doc += '.json'
                new_list.append(list_objs[i].to_dictionary())
                v1 = cls.to_json_string(new_list)
            with open(new_doc, 'w') as file:
                file.write(v1)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            json_string = []
            return json_string
        else:
            return (json.dumps(json_string))
