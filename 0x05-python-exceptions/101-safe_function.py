#!/usr/bin/python3
def safe_function(fct, *args):
    import sys
    try:
        return(fct(*args))
    except ZeroDivisionError as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
    except IndexError as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
