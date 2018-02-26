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


n, l = input(), [int(i) for i in input().strip().split()]
insertion_sort(l)
