#!/bin/python3

import sys

test_data = []
with open('data/plus_minus.txt') as data:
    for line in data:
        test_data.append(line.strip())

n = int(test_data[0])
arr = []
arr = [int(arr_temp) for arr_temp in test_data[1].split(' ')]


def plus_minus(n, arr):
    positive_nums = 0
    negative_nums = 0
    zeros = 0

    for num in arr:
        if num == 0:
            zeros += 1
        elif num > 0:
            positive_nums += 1
        else:
            negative_nums += 1

    print('{:.6f}'.format(positive_nums/n))
    print('{:.6f}'.format(negative_nums/n))
    print('{:.6f}'.format(zeros/n))

plus_minus(n, arr)
