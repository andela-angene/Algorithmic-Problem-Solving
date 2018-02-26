from collections import Counter


def migratory(n, ar):
    tracker = [0] * 5

    for i in ar:
        tracker[i - 1] += 1

    max_value = max(tracker)
    max_index = tracker.index(max_value)
    for i in range(5):
        if tracker[i] == max_value:
            max_index = min(max_index, i)

    return max_index + 1


#
#
# print(migratory(6, [1, 4, 4, 4, 5, 3]))
# print(migratory(6, [1, 1, 1, 2, 2, 2]))
# print(migratory(1, [3]))
# print(migratory(1, [3, 2]))


# Using counter
freq = Counter([1, 4, 4, 4, 5, 3])
print(max(freq, key=freq.get))
