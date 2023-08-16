imple_delete(a_dictionary, key=""):
    if key in a_dictionary:
"""Check if the key exists in the dictionary"""
        del a_dictionary[key]
"""Delete the key and its associated value"""
    return a_dictionary 
