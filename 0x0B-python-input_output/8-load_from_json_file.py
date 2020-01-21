#!/usr/bin/python3
import json


def load_from_json_file(filename):
    with open(filename, "r") as new_obj:
        data = json.loads(new_obj.read())
        return data
