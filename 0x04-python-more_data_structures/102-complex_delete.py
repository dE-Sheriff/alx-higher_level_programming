#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tmp_dict = a_dictionary.copy()
    for i in tmp_dict:
        if a_dictionary.get(i) is not None and a_dictionary[i] == value:
            del a_dictionary[i]
    return a_dictionary
