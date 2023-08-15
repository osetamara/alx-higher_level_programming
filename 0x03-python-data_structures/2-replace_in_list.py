#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replace an element of a list at a specific position.    
    Args:
        my_list (list): The list in which to replace the element.
        idx (int): The index of the element to replace.
        element: The new element to place at the specified index.    
    """
    # Check if the index is within valid bounds
    if idx >= 0 and idx < len(my_list):
        # Replace the element at the specified index
        my_list[idx] = element
    # Return the modified list
    return my_list
