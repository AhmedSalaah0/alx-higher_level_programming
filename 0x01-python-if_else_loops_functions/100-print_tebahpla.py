#!/usr/bin/python3
char = 122
for i in range(26):
    if i % 2 == 0:
        print(chr(char), end="")
        char -= 1
    else:
        print(chr(char - 32), end="")
        char -= 1
