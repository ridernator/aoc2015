#!/usr/bin/env python

inputFile = open("../data/input", "r")

x = [0, 0]
y = [0, 0]

houses = {
    "0#0": 1
}

index = 0
for direction in inputFile.read():
    match direction:
        case '^':
            y[index] += 1
        case 'v':
            y[index] -= 1
        case '>':
            x[index] += 1
        case '<':
            x[index] -= 1

    houses[str(x[index]) + '#' + str(y[index])] = 1

    index = (index + 1) % 2

print("Number of houses which receive at least one present :", len(houses))
