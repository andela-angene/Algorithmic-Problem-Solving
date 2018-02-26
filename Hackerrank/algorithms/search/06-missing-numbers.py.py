#!/bin/python3

import sys
data = []
with open('data/06-missing-numbers.py.txt') as file:
    for line in file:
        data.append(line.strip())


n, numbers = data[0], data[1].strip().split()
n2, permutations = data[2], data[3].strip().split()
cache = {}

for n in permutations:
    cache[n] = 1 if n not in cache else (cache[n] + 1)
for n in numbers:
    cache[n] -= 1

result = set()

for key in cache:
    if cache[key] > 0:
        result.add(key)

result = sorted(result, key=int)
print(' '.join(result))


### same solution using Counter by pyjac (python 2.7)
# from collections import Counter
#
# _, A, _, B = input(), map(int, raw_input().split(" ")), input(), map(int, raw_input().split(" "))
# ADict, BDict = Counter(A), Counter(B)
# result = []
# for (k, v) in ADict.items():
#     if BDict[k] != v:
#         result.append(k)
# print
# ' '.join(map(str, result))
