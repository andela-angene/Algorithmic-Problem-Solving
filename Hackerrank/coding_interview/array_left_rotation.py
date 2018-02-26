def array_left_rotation(arr, n, rotation):
    rotation = n - rotation % n
    result = [0] * n

    for i, item in enumerate(arr):
        rotate = (i + 1 + rotation) % n
        result[rotate - 1] = arr[i]

    return result


print(array_left_rotation([1, 2, 3, 4, 5], 5, 4))
print(array_left_rotation([1, 2, 3, 4, 5], 5, 6))
