import bisect


def minimum_loss(n, ar):
    minimum = ar[0]
    maximum = ar[0]
    min_diff = None
    seen = [maximum]

    for i in range(1, n):
        item = ar[i]
        if item < minimum:
            diff = minimum - item
            minimum = item
            if min_diff is None or diff < min_diff:
                min_diff = diff
        elif item > maximum:
            maximum = item
        elif minimum < item < maximum:
            position = bisect.bisect_right(seen, item)
            bisect.insort_right(seen, item)
            diff = seen[position + 1] - item
            if min_diff is None or diff < min_diff:
                min_diff = diff
            continue
        bisect.insort(seen, item)

    return min_diff


# n, ar = int(input().strip()), [int(i) for i in input().strip().split()]

print(minimum_loss(3, [5, 10, 3]))  # 2
print(minimum_loss(5, [20, 7, 8, 2, 5]))  # 2
print(minimum_loss(5, [18, 20, 10, 15, 2]))  # 3


# Todo: Understand this
# n = int(input())
#
# l = [int(item) for item in input().split()]
# l2 = l.copy()
# d = {}
# for i in range(len(l)):
#     d[l[i]] = i
# l = sorted(l)
# m = float("inf")
# for i in range(len(l) - 1):
#     if d[l[i + 1]] < d[l[i]]: m = min(m, l[i + 1] - l[i])
# print(m)
