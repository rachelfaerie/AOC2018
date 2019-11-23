# Advent of Code Day 2
# Scan a text file to find similar IDs
import collections
input_file = open("day2.txt", "r")
lines = input_file.readlines()


def part_one():
    double_counter = 0
    triple_counter = 0
    for line in lines:
        char_counter = collections.defaultdict(int)
        for char in line.strip():
            char_counter[char] += 1
        frequency_set = set(char_counter.values())
        if 2 in frequency_set:
            double_counter += 1
        if 3 in frequency_set:
            triple_counter += 1
    print(double_counter * triple_counter)


def hamming_distance(s1, s2):
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(el1 != el2 for el1, el2 in zip(s1, s2))


# noinspection PyShadowingNames
def find_strings_of_distance_one(lines):
    for i in range(len(lines)):
        for j in range(i+1, len(lines)):
            line1 = lines[i].strip()
            line2 = lines[j].strip()
            if hamming_distance(line1, line2) == 1:
                return line1, line2
    return None


def part_two():
    line1, line2 = find_strings_of_distance_one(lines)

    # Make a new string with all common characters of line 1 and line 2
    line3 = ""

    for i in range(len(line1)):
        if line1[i] == line2[i]:
            line3 += line1[i]

    print(line3)


part_one()
part_two()
