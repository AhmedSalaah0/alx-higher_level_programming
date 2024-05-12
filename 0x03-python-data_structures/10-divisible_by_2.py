#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    resultList = my_list
    for i in my_list:
        if my_list[i] % 2 == 0:
            resultList[i] = True
        else:
            resultList[i] = False
    return resultList
