#!/usr/bin/python3

def no_c(my_string):
    """
    Remove all occurrences of characters 'c' and 'C' from a string.
    
    Args:
        my_string (str): The input string from which to remove 'c' and 'C' characters.
        
    Returns:
        str: A new string with 'c' and 'C' characters removed.
    """
    # Create a copy of the string without 'c' and 'C' characters
    copy = [x for x in my_string if x != 'c' and x != 'C']
    
    # Join the characters in the list to form a new string
    new_string = "".join(copy)
    
    # Return the new string without 'c' and 'C' characters
    return new_string
