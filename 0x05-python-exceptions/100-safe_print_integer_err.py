#!/usr/bin/python3
def safe_print_integer_err(value):
    import sys
    test = 0
    try:
        print("{:d}".format(value))
    except Exception as i:
        sys.stderr.write("Exception: {}\n".format(i))
        return (False)
    else:
        return (True)
