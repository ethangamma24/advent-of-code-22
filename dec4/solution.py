#!/bin/python3

fully_contained_count = 0

def main():
    input = open('input.txt', 'r')
    lines = input.readlines()

    #partOne(lines)
    partTwo(lines)

def partOne(lines):
    global fully_contained_count

    for line in lines:
        fully_contained_count += checkPairsOne(line)

    print(fully_contained_count)

def partTwo(lines):
    global fully_contained_count

    for line in lines:
        fully_contained_count += checkPairsTwo(line)

    print(fully_contained_count)

def checkPairsOne(line):
    first = line[0:line.index(",")]
    second = line[line.index(",") + 1:]

    pair_one = [first[0:first.index("-")], first[first.index("-") + 1:]]
    pair_two = [second[0:second.index("-")], second[second.index("-") + 1:len(second)-1]]

    if (int(pair_one[0]) <= int(pair_two[0]) and int(pair_one[1]) >= int(pair_two[1])) or (int(pair_two[0]) <= int(pair_one[0]) and int(pair_two[1]) >= int(pair_one[1])):
        return 1
    else:
        return 0

    print(pair_one)
    print(pair_two)

def checkPairsTwo(line):
    first = line[0:line.index(",")]
    second = line[line.index(",") + 1:]

    pair_one = [first[0:first.index("-")], first[first.index("-") + 1:]]
    pair_two = [second[0:second.index("-")], second[second.index("-") + 1:len(second)-1]]

    if (
        int(pair_one[0]) in range(int(pair_two[0]), int(pair_two[1]) + 1) or 
        int(pair_one[1]) in range(int(pair_two[0]), int(pair_two[1]) + 1) or 
        int(pair_two[0]) in range(int(pair_one[0]), int(pair_one[1]) + 1) or 
        int(pair_two[1]) in range(int(pair_one[0]), int(pair_one[1]) + 1) 
    ):
        print(pair_one)
        print(pair_two)
        print()
        return 1
    else:
        return 0


main()
