#!/bin/python3

import sys
test_data = []
with open('data/maximum-element.txt') as data:
  for line in data:
    test_data.append(line.strip())

n = int(test_data[0])
stack = []
max_number = None

def max_element(el):
  global max_number
  if el[0] == '1':
    num = int(el[2:])
    if max_number == None or num > max_number:
      max_number = num
    stack.append(num)
  elif el[0] == '2':
    removed = stack.pop()
    if len(stack) == 0:
      max_number = None
    elif max_number == int(removed):
      max_number = max(stack)
  elif el[0] == '3':
    print(max_number)


for i in range(n):
  max_element(test_data[i + 1])
