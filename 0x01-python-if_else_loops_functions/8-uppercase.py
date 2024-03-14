#!/usr/bin/python3
def uppercase(str):
    res = ""
    for i in range(len(str)):
        if(ord(str[i]) >= 97 and ord(str[i]) <= 123):
          res += chr(ord(str[i]) - 32)
    print("{}".format(res))
