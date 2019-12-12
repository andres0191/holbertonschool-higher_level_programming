#!/usr/bin/python3
from calculator_1 import add
from calculator_1 import sub
from calculator_1 import mul
from calculator_1 import div
a = 10
b = 5
add_0 = int(a) + int(b)
res_0 = int(a) - int(b)
mul_0 = int(a) * int(b)
div_0 = int(a) // int(b)
print("{} + {} = {}".format(a, b, add_0))
print("{} - {} = {}".format(a, b, res_0))
print("{} * {} = {}".format(a, b, mul_0))
print("{} / {} = {}".format(a, b, div_0))
