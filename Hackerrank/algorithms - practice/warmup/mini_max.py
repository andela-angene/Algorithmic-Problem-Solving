def mini_max(arr):
    total = sum(arr)
    minimum = total - arr[0]
    maximum = total - arr[0]

    for i in range(1, 5):
        if total - arr[i] > maximum:
            maximum = total - arr[i]
        if total - arr[i] < minimum:
            minimum = total - arr[i]

    print(minimum, maximum)

mini_max([1, 2, 3, 4, 5])
