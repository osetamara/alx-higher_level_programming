#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Get the length of a string and its first character.
    
    Args:
        sentence (str): The input string for which to determine length and first character.
        
    Returns:
        tuple: A tuple containing two values: the length of the string and its first character.
    """
    # Check if the sentence is empty
    if sentence == "":
        # Return 0 length and None for first character
        return (0, None)
    
    # Return the length of the sentence and its first character
    return (len(sentence), sentence[0])
