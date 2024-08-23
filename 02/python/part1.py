#!/usr/bin/env python

inputFile = open("../data/input", "r")

totalArea = 0

for line in inputFile.readlines():
    dimensions = line.split("x")
    length = int(dimensions[0])
    width = int(dimensions[1])
    height = int(dimensions[2])

    area = 2 * (width * height + width * length + height * length)

    slack = min(width * height,
                width * length,
                height * length)

    totalArea += area + slack

print("Total area is", totalArea, "square feet")
