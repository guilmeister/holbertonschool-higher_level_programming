#!/usr/bin/python3
import sys
elements = len(sys.argv)
flag = 0
for numbers in range(0, elements):
    if elements == 1:
        if __name__ == '__main__':
            print("{:d} arguments.".format(elements - 1))
    elif elements == 2:
        flag = flag + 1
        if flag == 1:
            if __name__ == '__main__':
                print("{:d} argument:".format(elements - 1))
        else:
            if __name__ == '__main__':
                print("{:d}: {}".format(numbers, sys.argv[numbers]))
    elif elements > 2:
        flag = flag + 1
        if flag == 1:
            if __name__ == '__main__':
                print("{:d} arguments:".format(elements - 1))
        else:
            if __name__ == '__main__':
                print("{:d}: {}".format(numbers, sys.argv[numbers]))
