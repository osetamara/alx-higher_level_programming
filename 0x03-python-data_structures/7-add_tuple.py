#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Add two tuples element-wise.
    
    Args:
        tuple_a (tuple): The first tuple to be added. Defaults to (0, 0) if not provided.
        tuple_b (tuple): The second tuple to be added. Defaults to (0, 0) if not provided.
        
    Returns:
        tuple: A new tuple containing the sum of corresponding elements from tuple_a and tuple_b.
    """
    # Handle cases where tuples have fewer than 2 elements
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
        else:
            tuple_a = tuple_a[0], 0
    
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            tuple_b = tuple_b[0], 0
    
    # Calculate the sum of corresponding elements and return as a new tuple
    result_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return result_tuple
