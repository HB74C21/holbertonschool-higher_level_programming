#!/usr/bin/python3
def common_elements(set_1, set_2):
    new_set = []
    for element_set_1 in set_1:
        for element_set_2 in set_2:
            if element_set_1 == element_set_2:
                new_set.append(element_set_1)

    return new_set
