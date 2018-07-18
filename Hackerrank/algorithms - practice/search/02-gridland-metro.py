#!/bin/python3

import sys

data = []
with open('data/02-gridland-metro.txt') as file:
    for line in file:
        data.append(line)

grid_x, grid_y, n = [int(i) for i in data[0].strip().split()]
counter, total_sum = {}, grid_x * grid_y

for i in range(n):
    row, min_x, max_x = data[1:][i].strip().split()
    min_x, max_x = int(min_x), int(max_x)

    if row not in counter:
        counter[row] = {
            'ranges': [[min_x, max_x]],
            'total': max_x - min_x + 1
        }
    else:
        total = counter[row]['total']
        ranges = counter[row]['ranges']
        no_overlap = True
        for j in range(len(ranges)):
            min_y, max_y = ranges[j]
            if (min_y <= min_x <= max_y) or (min_x <= min_y <= max_x):
                all_ranges = [min_y, min_x, max_x, max_y]
                min_c, max_c = min(all_ranges), max(all_ranges)
                counter[row]['ranges'][j] = [min_c, max_c]
                counter[row]['total'] += (max_c - min_c) - (max_y - min_y)
                no_overlap = False
        if no_overlap:
            counter[row]['ranges'].append([min_x, max_x])
            counter[row]['total'] += max_x - min_x + 1

for row in counter:
    total_sum -= counter[row]['total']

print(total_sum)



# // TODO: understand the code below
# from collections import defaultdict
#
# n, m, k = map(int, input().split())
#
# tracks = defaultdict(list)
# for _ in range(k):
#     row, c1, c2 = map(int, input().split())
#     tracks[row].append((c1, -1))
#     tracks[row].append((c2 + 1, 1))
#
# ans = 0
# for row in tracks:
#     tracks[row].sort()
#
#     prev = tracks[row][0][0]
#     depth = 1
#     for event in tracks[row][1:]:
#         if depth > 0:
#             ans += (event[0] - prev)
#
#         depth -= event[1]
#         prev = event[0]
#
# print(n * m - ans)
