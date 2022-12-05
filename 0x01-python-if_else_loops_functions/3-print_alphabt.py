#!/usr/bin/python3
number = 97
while number <= 122:
    if number != 101 and number != 113:
        print("{}".format(chr(number)), end="")
    number += 1
