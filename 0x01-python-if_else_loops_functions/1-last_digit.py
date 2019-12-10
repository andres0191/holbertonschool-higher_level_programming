#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
tn = number
if number < 0:
    number = -(number)
    ln = number % 10
if tn < 0:
    number = tn
    ln = -(ln)
    print("Last digit of", number, "is", ln, "and is less than 6 and not 0")
if ln > 5:
    print("Last digit of", number, "is", ln, "and is greater that 5")
if ln == 0:
    print("Last digit of", number, "is", ln, "and is 0")
