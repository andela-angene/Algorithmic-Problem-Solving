#!/bin/python3

import sys

# n = int(input().strip())
# unsorted = []
# unsorted_i = 0
# for unsorted_i in range(n):
#     unsorted_t = str(input().strip())
#     unsorted.append(unsorted_t)

# ar = list(map(int, input().strip().split(' ')))

V = int(input().strip())
n = int(input().strip())
ar = list(map(int, input().strip().split(' ')))

print(ar.index(V))
