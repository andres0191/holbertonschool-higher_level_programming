#!/usr/bin/python3
""" Write a Python script that fetches
    https://intranet.hbtn.io/status
"""

import urllib.request

if __name__ == "__main__":
    url = 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(str(html))))
        print("\t- utf8 content: {}".format(html.decode("utf-8")))
