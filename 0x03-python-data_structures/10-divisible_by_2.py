#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Identify if each element in a list is divisible by 2.
    
    Args:
        my_list (list): A list of integers. Defaults to an empty list if not provided.
        
    Returns:
        list: A list of Boolean values indicating if each element is divisible by 2.
    """
    # Initialize a list to store Boolean values
    multiples = []
    
    # Loop through the list to check divisibility by 2
    for num in my_list:
        # Append True if the number is divisible by 2, else append False
        multiples.append(num % 2 == 0)
    
    return multiples
