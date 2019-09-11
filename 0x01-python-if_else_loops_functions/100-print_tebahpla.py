#!/usr/bin/python3
for letters in range(122, 96, -1):
    if letters % 2 == 0:
        print("{:c}".format(letters), end="")
    else:
        print("{:c}".format(letters - 32), end="")
