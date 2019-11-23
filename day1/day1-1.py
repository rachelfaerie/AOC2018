# Advent of Code - Day 1 - Part 1
# Reads numbers from txt file and adds and subtracts them from an integer variable

input_file = open("day1.txt", "r")

frequency_1: int = 0

for line_1 in input_file.readlines():
    frequency_1 += int(line_1.strip())
print("The frequency is " + str(frequency_1))
