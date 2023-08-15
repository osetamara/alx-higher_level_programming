#!/usr/bin/python3
def element_at(my_list, idx):
    """
    Retrieve an element from a list at a specified index.    
    Args:
        my_list (list): The list from which to retrieve the element.
        idx (int): The index of the element to re
    Return:
        element: The element at the specified index, or None if the index is out of bounds.
    """
    # Check if the index is out of bounds
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    # Return the element at the specified index
    return my_list[idx]
