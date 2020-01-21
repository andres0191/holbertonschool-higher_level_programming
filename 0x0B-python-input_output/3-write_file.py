#!/usr/bin/python3
def write_file(filename="", text=""):
    with open(filename, "w") as w_file:
        return w_file.write(text)
