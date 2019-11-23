# Advent of Code - Day 1 - Part 1
# Reads numbers from txt file and adds and subtracts them from an integer variable

input_file = open("day1-1.txt", "r")

for line in input_file.readlines() :
    print(int(line.strip()))
