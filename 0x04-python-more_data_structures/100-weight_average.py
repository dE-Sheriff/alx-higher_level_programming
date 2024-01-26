#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    sums = 0
    divs = 0
    for i in my_list:
        sums += i[0] * i[1]
        divs += i[1]
    return sums / divs\
