#!/bin/python3

import sys
test_data = []
with open('data/apple_and_orange.txt') as data:
    for line in data:
        test_data.append(line.strip())


s, t = test_data[0].strip().split(' ')
s, t = [int(s), int(t)]
a, b = test_data[1].strip().split(' ')
a, b = [int(a), int(b)]
m, n = test_data[2].strip().split(' ')
m, n = [int(m), int(n)]
apple = [int(apple_temp) for apple_temp in test_data[3].strip().split(' ')]
orange = [int(orange_temp) for orange_temp in test_data[4].strip().split(' ')]


def apple_orange(home, trees, apples, oranges):
    apples_on_house = 0
    oranges_on_house = 0

    for apple in apples:
        position = trees[0] + apple
        if position >= home[0] and position <= home[1]:
            apples_on_house += 1

    for orange in oranges:
        position = trees[1] + orange
        if position >= home[0] and position <= home[1]:
            oranges_on_house += 1

    print(apples_on_house)
    print(oranges_on_house)


apple_orange([s, t], [a, b], apple, orange)
