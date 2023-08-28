#!/usr/bin/python3

def safe_print_integer(value):
""" print element with "{:d}".format().

  Arg:
    value(int):The integer t print

  Retrurn:
     if a valueErro occrs - false
     Otherwise - True.
"""
   try:
      print("{:d}".format(value))
             return (True)
    except (TypeError, ValueError):
        return (False)
