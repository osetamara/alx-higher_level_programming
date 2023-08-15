#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Delete an item from a list at a specific position.
    Args: my_list (list): list from which to delete an item.
      Defaults to an empty list if not provided.
        idx (int): The index of the item to be deleted.  
    """
    #Check if the index is within valid bounds
    if idx >= 0 and idx < len(my_list):
        #Use 'del' statement to remove item at specified index
        del my_list[idx]
    # Return the modified list
    return my_list
