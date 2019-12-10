#!/usr/bin/python3
def uppercase(str):
    for lether in str:
        if ord(lether) >= (97) and ord(lether) <= (122):
            lether = chr(ord(lether) - 32)
            print("{}".format(lether), end="")
        else:
            print("{}".format(lether), end="")
    print()
