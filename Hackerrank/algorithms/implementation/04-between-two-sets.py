#!/bin/python3

import sys
import math


def getFactors(max_a, min_b):
    factors = set()
    max_factor = math.floor(math.sqrt(min_b))
    n = 1

    while n <= max_factor:
        if min_b % n == 0:
            two_factors = [n, min_b / n]
            for factor in two_factors:
                if factor >= max_a and factor % max_a == 0:
                    factors.add(int(factor))
        n += 1

    return list(factors)


def get_total_x(a, b):
    factors = getFactors(max(a), min(b))

    for i in a:
        n = 0
        while n < len(factors):
            factor = factors[n]
            if factor % i != 0:
                factors.remove(factor)
                n -= 1
            n += 1

    for i in b:
        n = 0
        while n < len(factors):
            factor = factors[n]
            if i % factor != 0:
                factors.remove(factor)
                n -= 1
            n += 1

    return len(factors)


# print(getFactors(3, 12))
print(get_total_x([1], [72, 48]))  # 8
print(get_total_x([2, 6], [12]))  # 2
print(get_total_x([2, 4], [16, 32, 96]))  # 3
