#!/usr/bin/env python

file = open("../data/input", "r")
symbols = file.read()

floor = 0

for symbol in symbols:
    if (symbol == '('):
        floor += 1
    elif (symbol == ')'):
        floor -= 1

print("Ending floor is", floor)
