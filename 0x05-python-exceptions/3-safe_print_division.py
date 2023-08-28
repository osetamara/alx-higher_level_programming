#!/usr/bin/python3

def safe_print_division(a, b):
    """Returns the value division of a by b.
      Otherwise: none
    """
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)

