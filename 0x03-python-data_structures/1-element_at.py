#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Retrieve an element from a list at a specified index.    
    Args: my_list (list):list from which to retrieve element.
        idx (int): The index of element to re
    Return:
        element: element at a specified index.
    """
    # Check if the index is out of bounds
    if idx < 0 or idx > (len(my_list) - 1):
        return None
    # Return the element at the specified index
    return my_list[idx]
