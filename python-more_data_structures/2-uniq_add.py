#!/usr/bin/python3
def uniq_add(my_list=[]):
    add_uniq_number = 0
    for new_list in set(my_list):
        add_uniq_number = add_uniq_number + new_list
    return add_uniq_number
