#!/usr/bin/python3
import hidden_4
for string in dir(hidden_4):
    if string.startswith("__"):
        continue
    else:
        if __name__ == '__main__':
            print(string)
