#!/usr/bin/python3
for c in range(97, 123):
    if c is 101 or c is 113:
        continue
    print("{}".format(chr(c)), end="")
