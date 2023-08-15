#!/usr/bin/python3

def no_c(my_string):
    """
    Remove occurrences of characters 'c' and 'C' from a string.    
    """
    # Create a copy of string without 'c' and 'C' characters
    copy = [x for x in my_string if x != 'c' and x != 'C']
    # Join the characters in the list to form a new string
    new_string = "".join(copy)
    # Return the new string without 'c' and 'C' characters
    return new_string
