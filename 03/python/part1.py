#!/usr/bin/env python

inputFile = open("../data/input", "r")

x = 0
y = 0

houses = {
    "0#0": 1
}

for direction in inputFile.read():
    match direction:
        case '^':
            y += 1
        case 'v':
            y -= 1
        case '>':
            x += 1
        case '<':
            x -= 1

    houses[str(x) + '#' + str(y)] = 1

print("Number of houses which receive at least one present :", len(houses))
