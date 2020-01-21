#!/usr/bin/python3
import os
def read_file(filename=""):
    file_open = open("my_file_0.txt", "r")
    print (file_open.read())
    file_open.close