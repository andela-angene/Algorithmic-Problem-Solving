#!/bin/python3

import sys
data = []
with open('data/07-pairs.txt') as file:
    for line in file:
        data.append(line.strip())


n, k = [int(i) for i in data[0].strip().split()]
ar, result = [int(i) for i in data[1].strip().split()], 0

ar.sort()
pointer, last = len(ar) - 2, len(ar) - 1

while pointer > -1:
    diff = ar[last] - ar[pointer]
    while diff >= k:
        if diff == k:
            result += 1
            last -= 1
            break
        last -= 1
        diff = ar[last] - ar[pointer]
    pointer -= 1

print(result)
