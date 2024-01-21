#!/usr/bin/python3
def multiple_returns(sentence):
    str_len = len(sentence)
    first_chr = sentence[0]
    if (sentence == ""):
        first_chr = None
    return (str_len, first_chr)
