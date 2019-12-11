#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        x = ((number * -1) % 10)
        print("{}".format(int(x)), end="")
    else:
        x = number % 10
        print("{}".format(int(x)), end="")
    return(x)
