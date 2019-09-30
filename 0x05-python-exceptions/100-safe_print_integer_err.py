#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    flag = 0
    try:
        if(isinstance(value, int)):
            flag = 1
    except Exception as e:
        print(e)
    finally:
        if flag == 1:
            print("{:d}".format(value))
            return True
        else:
            return False
