#!/usr/bin/python3

if "__main__" == __name__:
    from calculator_1 import sub, add, mul, div
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, (add(a, b))))
    print("{:d} - {:d} = {:d}".format(a, b, (sub(a, b))))
    print("{:d} * {:d} = {:d}".format(a, b, (mul(a, b))))
    print("{:d} / {:d} = {:d}".format(a, b, (div(a, b))))
