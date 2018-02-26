#!/bin/python3
import bisect
import sys

data = []
with open('data/09-maximum-sub-array-sum.txt') as file:
    for line in file:
        data.append(line.strip())

# // accurate but slow
# def find_max_mod(n, m, ar):
#     max_m, max_mod, total_sum, sub_ar = m - 1, 0, 0, {}
#
#     for i in range(n):
#         for key in sub_ar:
#             total, length = sub_ar[key]
#             total += ar[i] - ar[i - length]
#             if total % m == max_m:
#                 return max_m
#             max_mod = max(max_mod, total % m)
#             sub_ar[key] = [total, length]
#
#         total_sum += ar[i]
#         if total_sum % m == max_m:
#             return max_m
#         max_mod = max(max_mod, total_sum % m)
#         sub_ar[str(i + 1)] = [total_sum, (i + 1)]
#
#     return max_mod


def find_max_mod(n, m, ar):
    ar[0] = ar[0] % m
    sub, max_mod = [], 0

    for i in range(1, n):
        ar[i] = (ar[i - 1] + ar[i]) % m

    for i in range(n):
        item = ar[i]
        position = bisect.bisect_right(sub, item)
        j = sub[position] if position < i else 0
        if j > item:
            max_mod = max(max_mod, (item - j + m) % m)
        bisect.insort(sub, item)
        max_mod = max(max_mod, item)

    return max_mod


tn = int(data[0].strip())

for t in range(0, tn + 1, 2):
    nn, mm = [int(i) for i in data[t + 1].strip().split()]
    arr = [int(i) for i in data[t + 2].strip().split()]

    print(find_max_mod(nn, mm, arr))
