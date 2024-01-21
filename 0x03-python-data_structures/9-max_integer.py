#!/usr/bin/python3
def max_integer(my_list=[]):
    biggest_int = 0
    for num in my_list:
        if num > biggest_int:
            biggest_int = num
    return biggest_int
