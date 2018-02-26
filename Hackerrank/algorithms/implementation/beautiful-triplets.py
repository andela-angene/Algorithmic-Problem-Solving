import bisect


def find_next_value(series, i, diff):
    next_value = series[i] + diff
    index = bisect.bisect_left(series, next_value)
    is_next = True if index != len(series) and series[index] == next_value \
        else False
    return is_next, index, next_value


def beautiful_triplets_v1(diff, series):
    beautiful, length = 0, len(series)
    for i in range(length):
        is_next, index, next_value = find_next_value(series, i, diff)
        if is_next:
            is_next = find_next_value(series, index, diff)[0]
            if is_next:
                beautiful += 1
    return beautiful


# Less Efficient but way shorter!
def beautiful_triplets(diff, series):
    beautiful, length = 0, len(series)
    for number in series:
        if (number - diff) in series and (number + diff) in series:
            beautiful += 1
    return beautiful


print(beautiful_triplets(3, [1, 2, 4, 5, 7, 8, 10]))
print(beautiful_triplets(5, [5, 10, 15, 20]))


# WOW - short solution! by Imortal_ks
"""
n,d = 7, 3
A = [1, 2, 4, 5, 7, 8, 10]
count = 0
A = set(A)
for x in A:
    if (x-d) in A and (x+d) in A:count+=1
print(count)
"""
