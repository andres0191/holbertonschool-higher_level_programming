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
        print("No result")
    r = post(url, data={'letter': letter}).json()

