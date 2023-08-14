#!/usr/bin/python3

def print_list_integer(my_list=None):
    """
    Print all integers in the given list.
    
    Args:
        my_list (list): A list containing integers.to an empty list if not provided.
    """
    # If no list is provided, create an empty list
    if my_list is None:
        my_list = []

    # Loop through the integers in the list
    for num in my_list:
        # Print each integer with proper formatting
        print("{:d}".format(num))
