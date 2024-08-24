#!/usr/bin/env python

def atLeast3Vowels(string):
    count = 0

    for char in 'a' 'e' 'i' 'o' 'u':
        count += string.count(char)

    return (count >= 3)


def contains2InARow(string):
    for index in range(0, len(string) - 1):
        if (string[index] == string[index + 1]):
            return True

    return False


def stringContains(string, testStrings):
    for testString in testStrings:
        if testString in string:
            return True

    return False


inputFile = open("../data/input", "r")

badStrings = ["ab", "cd", "pq", "xy"]

numNiceStrings = 0

for string in inputFile.readlines():
    string = string.strip()

    if (stringContains(string, badStrings)):
        continue

    if (not atLeast3Vowels(string)):
        continue

    if (not contains2InARow(string)):
        continue

    numNiceStrings += 1

print("Number of nice strings:", numNiceStrings)
