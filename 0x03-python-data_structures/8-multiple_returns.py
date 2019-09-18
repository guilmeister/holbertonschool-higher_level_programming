#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    if sentence is not '':
        return (length, sentence[0])
    return (length, None)
