#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
flag = 0
if number < 0:
    flag = 1
    last = number * -1
    last = last % 10
else:
    last = number % 10
if last == 0:
    print("Last digit of {:d} is {:d} and is 0".format(number, last))
elif last > 5 and flag == 1:
    last = last * -1
    print("Last digit of {:d} is {:d} and\
 is less than 6 and not 0".format(number, last))
elif last > 5:
    print("Last digit of {:d} is {:d} and\
 is greater than 5".format(number, last))
else:
    if flag == 1:
        last = last * -1
    print("Last digit of {:d} is {:d} and\
 is less than 6 and not 0".format(number, last))
