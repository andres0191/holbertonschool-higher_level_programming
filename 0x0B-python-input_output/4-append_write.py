#!/usr/bin/python3
def append_write(filename="", text=""):
    with open(filename, "a") as agg_txt:
        return agg_txt.write(text)
