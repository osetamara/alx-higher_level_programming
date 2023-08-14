#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """
    Replace an element in a copied list at a specific position.
    
    Args:
        my_list (list): The original list from which to create a copy and replace an element.
        idx (int): The index of the element to replace in the copied list.
        element: The new element to place at the specified index in the copied list.
        
    Returns:
        list: A new list with the specified element replaced, or the original list if index is out of bounds.
    """
    # Check if the index is out of bounds
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    
    # Create a copy of the original list
    copy = [x for x in my_list]
    
    # Replace the element at the specified index in the copied list
    copy[idx] = element
    
    # Return the modified copied list
    return copy
