#!/bin/python3

import sys
data = []
with open('data/08-sherlock-and-array.txt') as file:
    for line in file:
        data.append(line.strip())


def check_mirror(n, ar):
    if n < 2:
        return 'YES'
    ar_sum, prev_sum = sum(ar) - ar[0], 0
    for j in range(1, n):
        if ar_sum == prev_sum:
            return 'YES'
        prev_sum += ar[j - 1]
        ar_sum -= ar[j]

    return 'NO'


tn = int(data[0].strip())

for i in range(0, tn + 1, 2):
    n, ar = int(data[i + 1].strip()), [int(i) for i in data[i + 2].strip().split()]

    print(check_mirror(n, ar))


