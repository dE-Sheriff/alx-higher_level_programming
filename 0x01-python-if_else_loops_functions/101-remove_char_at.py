#!/usr/bin/python3
def remove_char_at(str, n):
    new_s = []
    for idx, i in enumerate(str):
        if idx == n:
            continue
        new_s.append(i)
    return "".join(new_s)
