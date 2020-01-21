#!/usr/bin/python3
def number_of_lines(filename=""):
    with open(filename, "r") as line:
        count = 0
        for number in line:
            count += 1
    return count
