#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
     list_ord = list(a_dictionary.keys())  # Get a list of keys from the dictionary
    list_ord.sort()  # Sort list of keys in alphabetical order
    
    for i in list_ord:  # Iterate through the sorted list of keys
        value = a_dictionary.get(i)
        print("{}: {}".format(i, value)) 
