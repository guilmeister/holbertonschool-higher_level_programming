#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence is None:
        return (0, None)
    else:
        length = len(sentence)
        first = ''
        for char in sentence:
            first = char
            break
        return (length, first)
