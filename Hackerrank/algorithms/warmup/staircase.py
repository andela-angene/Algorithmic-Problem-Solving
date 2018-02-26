#!/bin/python3

import sys


def staircase(n):
    stairs = [' '] * n
    for i in range(n):
        stairs[n - i - 1] = '#'
        print(''.join(stairs))

num = 6
staircase(num)
