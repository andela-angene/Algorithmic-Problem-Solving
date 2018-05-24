#!/bin/python3
import os

data = []
with open(os.environ['HOME'] + '/Documents/code/algorithms/hackerrank/algorithms/graph-theory/data/02-journey-to-the-moon.txt') as file:
    for line in file:
        data.append(line)


def find_connected(n, adjacency):
    queue, i = [n], 0
    adjacency[n]['visited'] = True
    while i < len(queue):
        vertex = adjacency[queue[i]]
        for item in vertex['nodes']:
            if not adjacency[item]['visited']:
                queue.append(item)
                adjacency[item]['visited'] = True
        i += 1
    return i


total, connected = map(int, data[0].strip().split())
adjacency, result, total_count = {}, 0, 0

for i in range(connected):
    pair = [int(i) for i in data[i + 1].strip().split()]

    for j in range(2):
        x, y = pair[j], pair[(j + 1) % 2]
        if x not in adjacency:
            adjacency[x] = {
                'nodes': [y],
                'visited': False
            }
        else:
            adjacency[x]['nodes'].append(y)

for i in adjacency:
    if not adjacency[i]['visited']:
        count = find_connected(i, adjacency)
        total_count += count
        result += count * (total - count)
result += (total - total_count) * (total - 1)

print(result // 2)

# TODO: Learn about python Deque
