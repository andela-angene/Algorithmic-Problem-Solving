def find_station(index, k, ar):
    distance, minimum = 0, ar[index]

    while index < len(ar):
        distance = ar[index] - minimum
        if distance > k:
            return index - 1
        index += 1
    return -1


def min_transmitters(n, k, ar):
    ar.sort()
    counter, location = 0, 0

    while location != -1:
        counter += 1
        location = find_station(location, k, ar)
        if location != -1:
            location = find_station(location, k, ar)
            if location == -1 or location >= n:
                break
            location += 1

    print(counter)


# num, k_num = [int(i) for i in input().strip().split()]
# arr = [int(i) for i in input().strip().split()]
# min_transmitters(num, k_num, arr)


min_transmitters(5, 1, [1, 2, 3, 4, 5])  # 2
min_transmitters(6, 1, [1, 2, 3, 4, 5, 6])  # 2
min_transmitters(7, 1, [1, 2, 3, 4, 5, 6, 7])  # 3
min_transmitters(8, 2, [7, 2, 4, 6, 5, 9, 12, 11])  # 3
min_transmitters(2, 2, [330, 600])  # 2
min_transmitters(2, 2, [330, 331])  # 1
