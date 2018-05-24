def solution(A, K):
    length = len(A)
    if length < 1:
        return []
    rotate = K % length
    result = [0] * length

    for i in range(0, length):
        result[(i + rotate) % length] = A[i]

    return result


def rotate(list, count):
    length = len(list)
    first = list[length - 1:]
    second = list[:length - 1]
    new_array = first + second
    if count <= 1:
        return new_array
    else:
        count -= 1
        return rotate(new_array, count)


print(rotate([3, 8, 9, 7, 6], 3))  # 9, 7, 6, 3, 8
print(rotate([3, 8, 9, 7, 6], 1))  # 6, 3, 8, 9, 7
print(rotate([3, 8, 9, 7, 6], 10))  # 3, 8, 9, 7, 6
print(rotate([3], 5))  # [3]
print(rotate([], 5))  # []
