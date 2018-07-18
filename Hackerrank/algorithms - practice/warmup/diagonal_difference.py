#!/bin/python3

import sys
test_data = []
with open('data/diagonal_difference.txt') as data:
    for line in data:
        test_data.append(line.strip())

n = int(test_data[0])
a = []
for a_i in range(n):
    a_t = [int(a_temp) for a_temp in test_data[a_i + 1].strip().split(' ')]
    a.append(a_t)

def dia_diff(n, rows):
    n = n - 1
    sum_first_diagonal = 0
    sum_second_diagonal = 0
    counter = 0
    for row in rows:
        sum_first_diagonal += row[counter]
        sum_second_diagonal += row[n - counter]
        counter += 1

    return abs(sum_first_diagonal - sum_second_diagonal)

print(dia_diff(n, a))
