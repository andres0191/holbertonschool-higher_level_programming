#!/usr/bin/python3
""" Write a Python script that takes in a
    letter and sends a POST request to
    http://0.0.0.0:5000/search_user with
    the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    url = "http://0.0.0.0:5000/search_user"
    letter = sys.argv[1]
    if len(letter) > 1:
        data={'letter': letter}    
    else:
        data = {'q': ""}
    r = requests.post(url, data)
    try:
        r_json = r.json()
        if len(r_json) == 0:
            print("No result")
        else:
            print("[{}] {}".format(r_json.get('id'), r_json.get('name')))
    except:
        print("Not a valid JSON")