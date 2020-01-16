#!/usr/bin/python
for i in range(ord('z'), ord('a') - 1, - 1):
    j = 0
    if i % 2 == 1:
        j = -32
    print("{}".format(chr(i + j)), end="")
