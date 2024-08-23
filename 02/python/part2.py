#!/usr/bin/env python

inputFile = open("../data/input", "r")

totalLength = 0

for line in inputFile.readlines():
    dimensions = line.split("x")
    length = int(dimensions[0])
    width = int(dimensions[1])
    height = int(dimensions[2])

    minPerimeter = min(2 * (length + width),
                       2 * (length + height),
                       2 * (width + height))

    bowLength = length * width * height

    totalLength += minPerimeter + bowLength

print("Total ribbon length is", totalLength, "feet")
