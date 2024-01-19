#!/usr/bin/python3

if "__main__" == __name__:
    import sys
    total = 0
    arg_len = len(sys.argv) - 1
    for num in range(arg_len):
        total += int(sys.argv[num + 1])
    print(total)
