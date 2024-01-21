#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    
    a1 = tuple_a[0] if len(tuple_a) > 0 and tuple_a[0] is not None else 0
    b1 = tuple_b[0] if len(tuple_b) > 0 and tuple_b[0] is not None else 0
    a2 = tuple_a[1] if len(tuple_a) > 1 and tuple_a[1] is not None else 0
    b2 = tuple_b[1] if len(tuple_b) > 1 and tuple_b[1] is not None else 0
    x = a1+b1
    y = a2+b2
    return tuple((a1+b1, a2+b2),)
