#!/usr/bin/env python

def rule1(string):
    for index in range(0, len(string) - 3):
        subString = string[index:index + 2]

        if (subString in string[index + 2:]):
            return True

    return False


def rule2(string):
    for index in range(0, len(string) - 2):
        if (string[index] == string[index + 2]):
            return True

    return False


inputFile = open("../data/input", "r")

numNiceStrings = 0

for string in inputFile.readlines():
    string = string.strip()

    if (not rule1(string)):
        continue

    if (not rule2(string)):
        continue

    numNiceStrings += 1

print("Number of nice strings:", numNiceStrings)
