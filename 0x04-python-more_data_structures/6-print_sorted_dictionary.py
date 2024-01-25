#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = []
    for i in a_dictionary:
        keys.append(i)
    new_keys = sorted(keys)
    for i in new_keys:
        print("{}: {}".format(i, a_dictionary.get(i)))
