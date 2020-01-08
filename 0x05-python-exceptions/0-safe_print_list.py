#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    imp = True
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
#            count = 0
            count = count + 1
        except:
            break
    if (imp):
        print()
        return count
