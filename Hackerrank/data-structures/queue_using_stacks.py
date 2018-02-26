#!/bin/python3

import sys
test_data = []
with open('data/queue_using_stacks.txt') as data:
    for line in data:
        test_data.append(line.strip())

n = int(test_data[0])
stack = []
front = None


def queue_using_stacks(el):
  global front
  if el[0] == '1':
    stack.append(int(el[2:]))
    if len(stack) == 1:
        front = stack[0]

  elif el[0] == '2':
    stack.pop(0)
    if len(stack) < 1:
        front = None
        return
    front = stack[0]

  elif el[0] == '3':
    print(front)

for i in range(n):
  queue_using_stacks(test_data[i + 1])
