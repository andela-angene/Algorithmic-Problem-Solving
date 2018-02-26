import math


def solution(x, y, d):
    return int(math.ceil((y - x) / float(d)))


print(solution(10, 85, 30))
print(solution(10, 11, 30))
print(solution(10, 21, 1))
