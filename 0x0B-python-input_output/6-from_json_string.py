#!/usr/bin/python3
import json


def from_json_string(my_str):
    string_json = json.loads(my_str)
    return string_json
