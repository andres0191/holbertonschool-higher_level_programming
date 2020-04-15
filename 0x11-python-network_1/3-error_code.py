#!/usr/bin/python3
""" Write a Python script that takes in a URL,
    sends a request to the URL and displays the
    body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
try:
    urllib.request.urlopen(url)
except urllib.error.HTTPError as e:
    html = response.read().decode('utf-8')
    print("Error code: {}".format(html))
