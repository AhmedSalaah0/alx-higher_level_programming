#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    for i in range(len(my_list)):
        repeted = False
        for j in range(i):
            if (my_list[i] == my_list[j] and i != j):
                repeted = True
        if not repeted:
            sum += my_list[i]
    return sum
