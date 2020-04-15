#!/usr/bin/python3
""" Write a Python script that takes in a
    URL and an email address, sends a POST
    request to the passed URL with the email
    as a parameter, and finally displays
    the body of the response.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload_dict = {"email": email}
    u = requests.post(url, data=payload_dict)
    print(u.text)
