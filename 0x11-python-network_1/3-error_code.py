#!/usr/bin/python3
""" Write a Python script that takes in a URL,
    sends a request to the URL and displays the
    body of the response (decoded in utf-8).
"""
import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    try:
        with request.urlopen(url) as response:
            decode_url = response.read().decode("utf-8")
            print(decode_url)
    except urllib.error.HTTPError as error:
        html = error.code
        print("Error code: {}".format(html))
