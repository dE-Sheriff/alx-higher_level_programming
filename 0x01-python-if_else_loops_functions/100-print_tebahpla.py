#!/usr/bin/python3
for idx, i in enumerate(reversed(range(97, 123))):
    print("{}".format(chr(i if idx % 2 == 0 else i - 32)), end="")
