#!/bin/python3

data = []
with open('data/01-roads-and-libraries.txt') as file:
    for line in file:
        data.append(line)


def find_connected(n, mapping):
    mapping[n]['visited'] = True
    count = 1
    for i in mapping[n]['nodes']:
        vertex = mapping[i]
        if not vertex['visited']:
            count += find_connected(i, mapping)
    return count


queries, track = int(data[0]), 0

for _ in range(queries):
    track += 1  # remove
    cities, roads, lib_cost, road_cost = [int(i) for i in data[track].strip().split()]
    mapping = {}

    for i in range(cities):
        mapping[i + 1] = {
            'nodes': [],
            'visited': False
        }

    for i in range(roads):
        track += 1  # remove
        pair = [int(i) for i in data[track].strip().split()]

        for j in range(2):
            mapping[pair[j]]['nodes'].append(pair[(j + 1) % 2])

    libs, repaired = 0, 0
    if lib_cost <= road_cost:
        libs = cities
    else:
        for n in mapping:
            item = mapping[n]
            if not item['visited']:
                libs += 1
                repaired += find_connected(n, mapping) - 1

    print((libs * lib_cost) + (repaired * road_cost))

# TODO: Understand the solution below
# from collections import defaultdict, deque
#
# for _ in range(int(input())):
#     n, m, x, y = map(int, input().split())
#     if x <= y:
#         print(n * x)
#         for _ in range(m):
#             input()
#     else:
#         nbhd = defaultdict(list)
#         for _ in range(m):
#             c1, c2 = map(int, input().split())
#             nbhd[c1].append(c2)
#             nbhd[c2].append(c1)
#         new_node = [True] * (n + 1)
#         count = 0
#         cache = deque()
#         for cur in range(1, n + 1):
#             if new_node[cur]:
#                 count += x
#                 cache.append(cur)
#                 new_node[cur] = False
#                 while cache:
#                     for i in nbhd[cache.popleft()]:
#                         if new_node[i]:
#                             cache.append(i)
#                             new_node[i] = False
#                             count += y
#         print(count)
