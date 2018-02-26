#!/bin/python3

import sys
test_data = []
with open('data/tale_of_two_stacks.txt') as data:
    for line in data:
        test_data.append(line.strip())

class MyQueue(object):
    def __init__(self):
        self.collection = []

    def peek(self):
        return self.collection[0]

    def pop(self):
        self.collection.pop(0)

    def put(self, value):
        self.collection.append(value)


queue = MyQueue()
t = int(test_data[0])
for line in range(t):
    values = map(int, test_data[line + 1].split())
    values = list(values)
    if values[0] == 1:
        queue.put(values[1])
    elif values[0] == 2:
        queue.pop()
    else:
        print(queue.peek())
