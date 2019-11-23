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


part_one()
