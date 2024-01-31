#!/usr/bin/python3
def max_integer(my_list=[]):
    my_list.sort()
    return None if not my_list else my_list[-1]
