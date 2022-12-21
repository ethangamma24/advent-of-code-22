#!/bin/python3
import sre_yield

priority_sum = 0
priority_map = {}

def main():
    input = open('input.txt', 'r')
    lines = input.readlines()
    
    #partOne(lines)
    partTwo(lines)

def partOne(lines):
    global priority_sum
    global priority_map

    count = 1

    for letter in sre_yield.AllStrings(r'[a-zA-Z]'):
        priority_map[letter] = count
        count += 1

    for line in lines:
        priority_sum += findDuplicatePriority(line)

    print(priority_sum)

def partTwo(lines):
    global priority_sum
    global priority_map

    count = 1

    for letter in sre_yield.AllStrings(r'[a-zA-Z]'):
        priority_map[letter] = count
        count += 1

    # Iterate over all lines in input by threes.
    for i in range(0, len(lines) - 2, 3):
        priority_sum += findGroupPriority(lines[i], lines[i+1], lines[i+2])
    print(priority_sum)

def findDuplicatePriority(line):
    compartment_size = int((len(line) - 1) / 2)
    second_compartment = line[compartment_size:]
    for i in range(0, compartment_size):
        if line[i] in second_compartment:
            return priority_map[line[i]]

def findGroupPriority(r_one, r_two, r_three):
    for char in r_one:
        if char in r_two and char in r_three:
            return priority_map[char]

main()
