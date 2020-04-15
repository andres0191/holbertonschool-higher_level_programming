#!/usr/bin/python3
""" Write a Python script that takes your Github
    credentials (username and password) and uses the
    Github API to display your id
"""

import requests
import sys

if __name__ == "__main__":
    url = "https://api.github.com/user"
    user = sys.argv[1]
    password = sys.argv[2]
    json = requests.get(url, auth=(user, password)).json()
    try:
        print(json["id"])
    except:
        print(None)
