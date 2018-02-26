#!/bin/python3

import sys
data = []
with open('data/03-ice-cream-parlor.txt') as file:
    for line in file:
        data.append(line.strip())


def ice_cream(amount, n, ar):
    seen = set()
    for i in range(n):
        diff = amount - ar[i]
        if diff in seen:
            return str(ar.index(diff) + 1), str(i + 1)
        seen.add(ar[i])


t = int(data[0].strip())
for i in range(1, t * 3, 3):
    amount, n = int(data[i].strip()), int(data[i + 1].strip())
    ar = [int(i) for i in data[i + 2].strip().split()]

    print(' '.join(ice_cream(amount, n, ar)))
