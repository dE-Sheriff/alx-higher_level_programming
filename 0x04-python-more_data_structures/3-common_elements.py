#!/usr/bin/python3
def common_elements(set_1, set_2):
    uniq_list = []
    for i in set_1:
        if i in set_2:
            uniq_list.append(i)
    return uniq_list
