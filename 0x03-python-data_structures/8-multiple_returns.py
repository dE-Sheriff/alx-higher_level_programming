#!/usr/bin/python3
def multiple_returns(sentence):
    if (sentence == ""):
        first_chr = None
        str_len = 0
    else:
        str_len = len(sentence)
        first_chr = sentence[0]
    return (str_len, first_chr)
