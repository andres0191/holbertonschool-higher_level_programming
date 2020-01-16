#!/usr/bin/python3
def magic_calculation(a, b):
    if a < b:
        ans = (a + b)
        for i in range(4, 6):
            ans = ans + i
        return ans
    else:
         return a - b
