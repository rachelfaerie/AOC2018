# Advent of Code - Day 1 - Part 1
# Reads numbers from txt file and adds and subtracts them from an integer variable

input_file = open("day1.txt", "r")

frequency: int = 0

for line in input_file.readlines():
    frequency += int(line.strip())
print(frequency)
