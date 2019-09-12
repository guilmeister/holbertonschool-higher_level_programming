#!/usr/bin/python3
import sys
elements = len(sys.argv)
summation = 0
for numbers in range(1, elements):
    summation = summation + int(sys.argv[numbers])
if __name__ == '__main__':
    print("{:d}".format(summation))
