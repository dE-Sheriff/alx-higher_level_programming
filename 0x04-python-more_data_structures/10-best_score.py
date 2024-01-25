#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_score = max(list(a_dictionary.values()))
    for i in a_dictionary:
        if a_dictionary[i] == max_score:
            return i
    return None
