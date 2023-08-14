#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Print all integers of a list in reverse order.
    
    Args:
        my_list (list): A list of integers. Defaults to an empty list if not provided.
    """
    # Check if the provided argument is a list
    if isinstance(my_list, list):
        # Reverse the order of the list
        my_list.reverse()
        
        # Loop through the reversed list and print each integer
        for i in my_list:
            print("{:d}".format(i))
