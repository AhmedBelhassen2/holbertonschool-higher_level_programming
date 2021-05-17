#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        rtat = a / b
    except:
        rtat = None
    finally:
        print("Inside result: {}".format(rtat))
        return rtat
