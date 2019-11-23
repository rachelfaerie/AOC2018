# Day 1 - Part 2
# Finds the first duplicate frequency (the first sum total that appears twice)

input_file = open("day1.txt", "r")

frequency = 0
numbers_seen = set()
loops = True
lines = input_file.readlines()

while loops:
    for line in lines:
        line = line.replace("\n", "")
        frequency += int(line)
        if frequency in numbers_seen:
            loops = False
            break
        else:
            numbers_seen.add(frequency)
print(frequency)