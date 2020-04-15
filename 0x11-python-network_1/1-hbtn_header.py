#!/usr/bin/python3
""" Write a Python script that takes in a URL,
    sends a request to the URL and displays the
    value of the X-Request-Id variable found in
    the header of the response.
"""
import urllib.request

url = 'https://intranet.hbtn.io/status'
with urllib.request.urlopen(url) as response:
    html = response.read()
    print(response.getheader('X-Request-Id'))
