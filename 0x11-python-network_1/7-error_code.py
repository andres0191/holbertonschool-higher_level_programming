#!/usr/bin/python3
""" Write a Python script that takes in a URL,
    sends a request to the URL and displays
    the body of the response.
"""
import requests
import sys

url = sys.argv[1]
try:
    r = requests.get(url)
    r.status_code
    print("Index")
except:
    print(r.status_code)