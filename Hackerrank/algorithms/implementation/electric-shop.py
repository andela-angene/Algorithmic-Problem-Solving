import bisect


def electric(N, M, s):
    N.sort()
    M.sort()
    result = -1
    for i in M:
        location = bisect.bisect_right(N, s - i)
        if location == 0:
            return result
        else:
            result = max(result, i + N[location - 1])
    return result


print(electric([3, 1], [5, 2, 8], 10))
print(electric([5], [4], 5))
