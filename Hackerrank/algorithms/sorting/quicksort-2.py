# n, l = input(), [i for i in input().strip().split()]


# print(' '.join(left + equal + right))


def partition(ar):
    left, right, equal, el = [], [], [ar[0]], int(ar[0])

    for i in range(1, len(ar)):
        if int(ar[i]) == el:
            equal.append(ar[i])
        elif int(ar[i]) > el:
            right.append(ar[i])
        else:
            left.append(ar[i])

    return left, equal, right


def quicksort(ar):
    if len(ar) < 2:
        return ar
    else:
        left, equal, right = partition(ar)
        result = quicksort(left) + equal + quicksort(right)
        print(' '.join(result))
        return result


print(quicksort(['5', '8', '1', '3', '7', '9', '2']), '===end====')
print(quicksort(['2', '3', '2', '2', '4']))


# print(quicksort([4, 5, 3, 7, 2]))
# print(quicksort([4, 3, 2, 1]))
# print(quicksort([4]))
# print(quicksort([4, 0]))
