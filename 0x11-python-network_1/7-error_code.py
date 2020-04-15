#!/usr/bin/python3
""" Write a Python script that takes in a URL,
    sends a request to the URL and displays
    the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        r = requests.get(url)
        print(r.text)-
    except:
        if r.status_code > 400:
            for line in r.status_code:
                print_ = ("Error code: {}".format(line.split(":")[0]))
