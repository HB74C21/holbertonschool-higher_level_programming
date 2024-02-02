#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    new_set = set_1.symmetric_difference(set_2)

    new_list = list(new_set)

    return new_list
