#!/usr/bin/env python

import numpy
import re

inputFile = open("../data/input", "r")

lights = numpy.zeros((1000, 1000), dtype=int)

for line in inputFile.readlines():
    match = re.search("(turn on|turn off|toggle) ([0-9]*),([0-9]*) through ([0-9]*),([0-9]*)", line.strip())

    command = match.group(1)
    x1 = int(match.group(2))
    y1 = int(match.group(3))
    x2 = int(match.group(4)) + 1
    y2 = int(match.group(5)) + 1

    if (command == "turn on"):
        for x in range(x1, x2):
            for y in range(y1, y2):
                lights[x][y] += 1
    elif (command == "turn off"):
        for x in range(x1, x2):
            for y in range(y1, y2):
                lights[x][y] -= 1

                if (lights[x][y] < 0):
                    lights[x][y] = 0
    elif (command == "toggle"):
        for x in range(x1, x2):
            for y in range(y1, y2):
                lights[x][y] += 2

totalBrightness = 0

for row in lights:
    for light in row:
        totalBrightness += light

print("Total brightness is", totalBrightness)
