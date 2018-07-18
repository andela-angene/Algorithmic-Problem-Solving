def insertion_sort(l):
    shifts = 0
    for i in range(1, len(l)):
        prev = i - 1
        current_item = l[i]
        while (prev >= 0) and (l[prev] > current_item):
            shifts += 1
            l[prev + 1] = l[prev]
            prev -= 1
        l[prev + 1] = current_item
    print(shifts)


# ar = [1, 4, 3, 5, 6, 2]
# ar = [8, 4, 3, 5, 6, 2]
ar = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
insertion_sort(ar)
print(ar)
