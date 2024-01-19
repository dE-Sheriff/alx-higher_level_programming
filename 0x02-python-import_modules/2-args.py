#!/usr/bin/python3

if "__main__" == __name__:
    import sys
    arg_len = len(sys.argv) - 1
    if arg_len == 1:
        print(f"{arg_len} argument:")
    elif arg_len == 0:
        print(f"{arg_len} arguments.")
    else:
        print(f"{arg_len} arguments:")
    for index in range(arg_len):
        print(f"{index + 1}: {sys.argv[index + 1]}")
