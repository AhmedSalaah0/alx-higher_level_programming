#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    dict = map(lambda x: x * 2, my_list)
    new_list = list(dict)
    return new_list
