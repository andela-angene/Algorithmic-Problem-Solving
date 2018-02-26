#!/bin/python3

import sys

test_data = []
with open('data/09-separate-the-numbers.py.txt') as data:
    for line in data:
        test_data.append(line.strip())


def find_next(current_el, current_i, text):
    next_el = str(int(current_el) + 1)
    next_len = len(next_el)
    next_i = current_i + len(current_el)
    if next_i >= len(text):
        return 'end'
    if next_el == text[next_i:next_i + next_len]:
        return next_el, next_i
    return False


def verify_pretty(current_el, current_i, text):
    while True:
        next_ar = find_next(current_el, current_i, text)
        if next_ar:
            if next_ar == 'end':
                return True
            current_el, current_i = next_ar
        else:
            return False


def separate_numbers(text):
    counter = 1
    first_n = text[:counter]
    while counter <= int(len(text) / 2) + 1:
        next_ar = find_next(first_n, 0, text)
        if next_ar and next_ar != 'end' and \
                verify_pretty(next_ar[0], next_ar[1], text):
            return 'YES {}'.format(first_n)
        counter += 1
        first_n = text[:counter]
    return 'NO'


q = int(test_data[0].strip())
for a0 in range(1, q + 1):
    s = test_data[a0].strip()
    print(separate_numbers(s))

# print(separate_numbers('910'))
# print(separate_numbers('99100101'))
# print(separate_numbers('101103'))


# Short solution, TODO: try to understand this
if __name__ == 'best-solution':
    for _ in range(int(input())):
        s = input().strip()
        n = len(s)
        x = ''
        for i in s[:-1]:
            x += i
            y = int(x)
            z = ''
            while len(z) < n:
                z += str(y)
                y += 1
            if n == len(z) and z == s:
                print("YES", x)
                break
        else:
            print("NO")
