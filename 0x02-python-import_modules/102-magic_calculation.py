#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub
    if a < b:
        ans = add(a, b)
        for i in range(4, 6):
            ans = add(ans, i)
        return ans
    else:
         return sub(a, b)
