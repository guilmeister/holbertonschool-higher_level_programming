#!/usr/bin/python3
def text_indentation(text):
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    x = 0
    while x < len(text):
        if text[x] == '.' or text[x] == '?' or text[x] == ':':
            print(text[x], end="")
            print("")
            print("")
            x = x + 1
            if text[x] == ' ':
                x = x + 1
        print(text[x], end="")
        x = x + 1
