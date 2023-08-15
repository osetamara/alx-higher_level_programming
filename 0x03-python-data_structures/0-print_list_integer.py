#!/usr/bin/python3

def print_list_integer(my_list=None):
    """
    Print all integers in the given list.
    """
    # If no list is provided, create an empty list
    if my_list is None:
        my_list = []
    # Loop through the integers in the list
    for num in my_list:
        # Print each integer with proper formatting
        print("{:d}".format(num))
