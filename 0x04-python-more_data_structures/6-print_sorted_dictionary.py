#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
     sort_keys = sort(a_dictionary.keys())  # Get a sort of keys from dictionary
    
    for key in sort_keys:  # Iterate through the sorted keys
        print("{}: {}".format(key, a_dictionary.get(key))) 
