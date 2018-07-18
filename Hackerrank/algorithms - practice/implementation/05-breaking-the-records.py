#!/bin/python3

import sys

test_data = []
with open('data/05-breaking-the-records.txt') as data:
    for line in data:
        test_data.append(line.strip())

data = list(map(int, test_data[1].split(' ')))


def break_records(numbers):
    max_n = [numbers[0], 0]
    min_n = [numbers[0], 0]

    for i in numbers:
        if i > max_n[0]:
            max_n[1] += 1
            max_n[0] = i
        if i < min_n[0]:
            min_n[1] += 1
            min_n[0] = i

    return max_n[1], min_n[1]


print(break_records(data))
