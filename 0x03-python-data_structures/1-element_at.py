#!/usr/bin/python3
def element_at(my_list, idx):
    if (0 - len(my_list)) > idx or idx > (len(my_list) - 1):
        return None
    else:
        return my_list[idx]
