#!/usr/bin/python3


def uppercase(str):
    result = ''
    for letters in str:
        if ord(letters) >= 97 and ord(letters) <= 122:
            result = result + chr(ord(letters) - 32)
        else:
            result = result + letters
    print(result)
