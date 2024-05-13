#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    sum = 0
    sum2 = 0
    for i in range(len(my_list)):
        sum += my_list[i][0] * my_list[i][1]
        sum2 += my_list[i][1]
    return sum / sum2
