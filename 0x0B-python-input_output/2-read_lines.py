#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    with open(filename, "r") as r_lines:
        count = 0
        for line in r_lines:
            if nb_lines == count and nb_lines > 0:
                break
            print(line, end="")
            count += 1
    r_lines.close
