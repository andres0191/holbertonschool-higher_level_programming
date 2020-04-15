#!/usr/bin/python3
"""Write a Python script that takes in a URL
    and an email, sends a POST request to the
    passed URL with the email as a parameter,
    and displays the body of the response
    (decoded in utf-8)
"""
import urllib.request
import urllib.parse
import sys

url = sys.argv[1]
email = sys.argv[2]
values = {'email': email}
data = urllib.parse.urlencode(values)
data = data.encode('utf-8')
with urllib.request.urlopen(url, data) as response:
    html = response.read().decode('utf-8')
    print(html)
