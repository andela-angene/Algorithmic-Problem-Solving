#!/bin/python3

data = []
with open('data/05-breadth-first-search-shortest-reach.txt') as file:
    for line in file:
        data.append(line)


def find_connected(n, adjacency):
    queue, i = [n], 0
    adjacency[n].breadth = 0
    while i < len(queue):
        vertex = adjacency[queue[i]]
        for item in vertex.nodes:
            if adjacency[item].breadth == -1:
                queue.append(item)
                adjacency[item].breadth = vertex.breadth + 6
        i += 1
    return True


class Vertex(object):
    def __init__(self, name):
        self.name = name
        self.nodes = []
        self.breadth = -1

    def __repr__(self):
        return 'Vertex({})'.format(self.name)


queries, track = int(data[0]), 0  # remove

for _ in range(queries):
    track += 1  # remove
    vertices, edges = [int(i) for i in data[track].strip().split()]
    graph, result = {}, ''

    for i in range(vertices):
        graph[i + 1] = Vertex(i + 1)

    for i in range(edges):
        track += 1  # remove
        pair = [int(i) for i in data[track].strip().split()]

        for j in range(2):
            graph[pair[j]].nodes.append(pair[(j + 1) % 2])
    track += 1  # remove
    source = int(data[track].strip())
    find_connected(source, graph)

    for i in range(vertices):
        if (i + 1) != source:
            result += str(graph[i + 1].breadth) + ' '
    print(result)
