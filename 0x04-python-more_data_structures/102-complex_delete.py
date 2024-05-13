#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    KeyToDelete = [k for k in a_dictionary if a_dictionary[k] == value]

    for k in KeyToDelete:
        a_dictionary.pop(k)
    return a_dictionary
