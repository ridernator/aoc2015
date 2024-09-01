#!/usr/bin/env python

import re

inputFile = open("../data/input", "r")

notPattern = re.compile("NOT.*")
andPattern = re.compile(".*AND.*")
orPattern = re.compile(".*OR.*")
rshiftPattern = re.compile(".*RSHIFT.*")
lshiftPattern = re.compile(".*LSHIFT.*")
wireToWirePattern = re.compile("[a-z]* -> [a-z]*")
numberToWirePattern = re.compile("[0-9]* -> [a-z]*")

wires = {}
wires["1"] = 1
wires["b"] = 16076

lines = inputFile.readlines()

while ("a" not in wires):
    for line in lines:
        line = line.strip()

        if (re.match(notPattern, line)):
            match = re.search("NOT ([a-z0-9]*) -> ([a-z]*)", line)
            fromWire = match.group(1)
            toWire = match.group(2)

            if ((fromWire in wires) and (toWire not in wires)):
                wires[toWire] = ~wires[fromWire]

                print(line, ": ", toWire, " set to NOT ", fromWire, "(", wires[fromWire], ") = ", ~wires[fromWire], sep='')
        elif (re.match(andPattern, line)):
            match = re.search("([a-z0-9]*) AND ([a-z0-9]*) -> ([a-z]*)", line)
            fromWire1 = match.group(1)
            fromWire2 = match.group(2)
            toWire = match.group(3)

            if ((fromWire1 in wires) and (fromWire2 in wires) and (toWire not in wires)):
                wires[toWire] = wires[fromWire1] & wires[fromWire2]

                print(line, ": ", toWire, " set to ", fromWire1, "(", wires[fromWire1], ") AND ", fromWire2, "(", wires[fromWire2], ") = ", wires[fromWire1] & wires[fromWire2], sep='')
        elif (re.match(orPattern, line)):
            match = re.search("([a-z0-9]*) OR ([a-z0-9]*) -> ([a-z]*)", line)
            fromWire1 = match.group(1)
            fromWire2 = match.group(2)
            toWire = match.group(3)

            if ((fromWire1 in wires) and (fromWire2 in wires) and (toWire not in wires)):
                wires[toWire] = wires[fromWire1] | wires[fromWire2]

                print(line, ": ", toWire, " set to ", fromWire1, "(", wires[fromWire1], ") OR ", fromWire2, "(", wires[fromWire2], ") = ", wires[fromWire1] | wires[fromWire2], sep='')
        elif (re.match(rshiftPattern, line)):
            match = re.search("([a-z0-9]*) RSHIFT ([0-9]*) -> ([a-z]*)", line)
            fromWire = match.group(1)
            shiftNum = int(match.group(2))
            toWire = match.group(3)

            if ((fromWire in wires) and (toWire not in wires)):
                wires[toWire] = wires[fromWire] >> shiftNum

                print(line, ": ", toWire, " set to ", fromWire, "(", wires[fromWire], ") >> ", shiftNum, " = ", wires[fromWire] >> shiftNum, sep='')
        elif (re.match(lshiftPattern, line)):
            match = re.search("([a-z0-9]*) LSHIFT ([0-9]*) -> ([a-z]*)", line)
            fromWire = match.group(1)
            shiftNum = int(match.group(2))
            toWire = match.group(3)

            if ((fromWire in wires) and (toWire not in wires)):
                wires[toWire] = wires[fromWire] << shiftNum

                print(line, ": ", toWire, " set to ", fromWire, "(", wires[fromWire], ") << ", shiftNum, " = ", wires[fromWire] << shiftNum, sep='')
        elif (re.match(wireToWirePattern, line)):
            match = re.search("([a-z]*) -> ([a-z]*)", line)
            fromWire = match.group(1)
            toWire = match.group(2)

            if ((fromWire in wires) and (toWire not in wires)):
                wires[toWire] = wires[fromWire]

                print(line, ": ", toWire, " set to ", fromWire, "(", wires[fromWire], ")", sep='')
        elif (re.match(numberToWirePattern, line)):
            match = re.search("([0-9]*) -> ([a-z]*)", line)
            number = int(match.group(1))
            toWire = match.group(2)

            if (toWire not in wires):
                wires[toWire] = number

                print(line, ": ", toWire, " set to ", number, sep='')
        else:
            print("No match for", line)

print("Signal on a is", wires["a"])
