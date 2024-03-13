#!/usr/bin/python3
for i in range(99):
    if i < 10:
        print("0{}".format(i), end=", ")
    else:
        print("{0:d}".format(i), end=", " if i < 99 else "")
