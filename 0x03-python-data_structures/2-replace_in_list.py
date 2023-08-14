#!/usr/bin/python3
# This script defines a function to replace an element in a list at a specific position.

def replace_in_list(my_list, idx, element):
    """
    Replace an element of a list at a specific position.
    
    Args:
        my_list (list): The list in which to replace the element.
        idx (int): The index of the element to replace.
        element: The new element to place at the specified index.
        
    Returns:
        list: The updated list with the replacement, or the original list if index is out of bounds.
    """
    # Check if the index is within valid bounds
    if idx >= 0 and idx < len(my_list):
        # Replace the element at the specified index
        my_list[idx] = element
    
    # Return the modified list
    return my_list
