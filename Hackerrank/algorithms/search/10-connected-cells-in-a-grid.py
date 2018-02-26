#!/bin/python3

data = []
with open('data/10-connected-cells-in-a-grid.txt') as file:
    for line in file:
        data.append(line.strip())


def find_connected_nodes(i, j, ar):
    ar[i][j]['unvisited'] = False
    count = 1
    neighbors = [[i, j+1], [i-1, j+1], [i-1, j], [i-1, j-1],
                 [i, j-1], [i+1, j-1], [i+1, j], [i+1, j+1]]
    for neighbor in neighbors:
        x, y = neighbor
        if x < 0 or y < 0:
            continue
        try:
            item = ar[x][y]
            if item['value'] == 1 and item['unvisited']:
                count += find_connected_nodes(x, y, ar)
        except IndexError:
            pass

    return count


r, c = int(data[0]), int(data[1])
ar = []

for i in range(2, r + 2):
    ar.append([{'value': int(i), 'unvisited': True} for i in data[i].strip().split()])

max_cluster = 0
for i in range(r):
    for j in range(c):
        item = ar[i][j]
        if item['value'] == 1 and item['unvisited']:
            connected = find_connected_nodes(i, j, ar)
            max_cluster = max(max_cluster, connected)
print(max_cluster)
