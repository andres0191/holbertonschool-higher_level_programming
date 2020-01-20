#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        copy_list = self.copy()
        copy_list.sort()
        print (copy_list)
