#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Find the biggest integer in a list.
    
    Args:
        my_list (list): A list of integers. Defaults to an empty list if not provided.
        
    Returns:
        int or None: The biggest integer in the list, or None if the list is empty.
    """
    # Check if the list is empty
    if len(my_list) == 0:
        return None
    
    # Initialize the variable to store the biggest integer
    biggest = my_list[0]
    
    # Loop through the list to find the biggest integer
    for num in my_list:
        if num > biggest:
            biggest = num
    
    return biggest
