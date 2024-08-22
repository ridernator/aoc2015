#!/usr/bin/env python

file = open("../data/input", "r")
symbols = file.read()

floor = 0
symbolIndex = 0

for symbol in symbols:
    symbolIndex += 1

    if (symbol == '('):
        floor += 1
    elif (symbol == ')'):
        floor -= 1

    if (floor == -1):
        break

print("Got to the basement at character", symbolIndex)
