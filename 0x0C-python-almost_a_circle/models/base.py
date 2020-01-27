#!/usr/bin/python3
""" Class Base """


import json


class Base:
    """ The first class for the project almost a circle"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ validate of id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ valid input list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return (json.dumps(list_dictionaries))

    @classmethod
    def save_to_file(cls, list_objs):
        """ protect with @classmethod the method save_to file
            and validate if is None. list_objs is a list of
            instance who inherits of base
        """
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
        """ json_string is a string representing a list of
            dictionaries. if json_string is none or empty,
            return an empty list.
        """
        if json_string is None or len(json_string) == 0:
            json_string = []
            return json_string
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ **dictionary ca be thought of as a double
            pointer to a dictionary
        """
        new_clas = cls.__name__
        if new_clas == "Rectangle":
            dummy = cls(23, 48)
        elif new_clas == "Square":
            dummy = cls(46)
        dummy.update(**dictionary)
        return(dummy)

    @classmethod
    def load_from_file(cls):
        """ load_from_file return a list of instances
            if the file doesn't exist, return an empty list
        """
        empty_list = []
        complete_name = cls.__name__+'.json'
        try:
            with open(complete_name, 'r') as f:
                instance = cls.from_json_string(f.read())
                instance_list = [cls.create(**line) for line in instance]
                return instance_list
        except OSError:
            return (empty_list)
