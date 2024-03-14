#!/usr/bin/python3
def print_last_digit(number):
    last = abs(number - (int)(number / 10) * 10)
    print(last, end="")

    return last
