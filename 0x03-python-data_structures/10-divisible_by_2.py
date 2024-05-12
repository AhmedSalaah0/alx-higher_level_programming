#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    resultList = []
    for i in my_list:
        if my_list[i] % 2 == 0:
            resultList.append(True)
        else:
            resultList.append(False)
    return resultList
