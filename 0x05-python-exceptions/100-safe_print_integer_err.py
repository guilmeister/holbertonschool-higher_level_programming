#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    try:
        print("{:d}".format(value))
        return True
    except Exception as error:
        print("Exception: {}\n".format(error), file=sys.stderr, end="")
        return False
