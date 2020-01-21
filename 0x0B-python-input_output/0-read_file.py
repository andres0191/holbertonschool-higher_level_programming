#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, "r") as file_open:
        for character in file_open:
            print(character, end="")
        file_open.close
