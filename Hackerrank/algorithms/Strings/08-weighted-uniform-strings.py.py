#!/bin/python3

import sys

test_data = []
with open('data/08-weighted-uniform-strings.py.txt') as data:
    for line in data:
        test_data.append(line.strip())


def uniform_strings(text):
    total_set = []
    mapping = {}
    current_c = None
    counter = 0
    for c in text:
        if c != current_c:
            current_c = c
            counter = 0
        counter += (ord(c) - 96)
        if c in mapping and counter > mapping[c]:
            mapping[c] = counter
        elif c not in mapping:
            mapping[c] = counter
            total_set.append(counter)

    return total_set, mapping


s = test_data[0].strip()
n = int(test_data[1].strip())

chars, char_map = uniform_strings(s)

for a0 in range(2, n + 2):
    value = int(test_data[a0].strip())
    info = 'No'
    for i in chars:
        if value % i == 0 and value <= char_map[chr(i + 96)]:
            info = 'Yes'
            break
    print(info)

# Best solution
if __name__ == 'best-solution':
    s = input().strip()
    cost = set()
    prev = ''
    count = 0
    for i in s:
        if i != prev:
            prev = i
            count = 0
        count += 1
        cost.add(count * (ord(i) - ord('a') + 1))
    for _ in range(int(input())):
        print("Yes" if int(input()) in cost else "No")
