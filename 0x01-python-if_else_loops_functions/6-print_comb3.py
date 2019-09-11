#!/usr/bin/python3
for outsidenum in range(0, 10):
    for insidenum in range(0, 10):
        if outsidenum == 8 and insidenum == 9:
            print("{:d}{:d}".format(outsidenum, insidenum), end="")
        elif outsidenum != insidenum and outsidenum < insidenum:
            print("{:d}{:d}".format(outsidenum, insidenum), end=", ")
print("")
