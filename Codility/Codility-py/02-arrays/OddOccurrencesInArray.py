def solution(A):
    length = len(A)
    A.sort()

    i = 0
    while i < length:
        if i == length - 1 or A[i] != A[i + 1]:
            return A[i]
        i += 2


print(solution([9, 3, 9]))  # 3
print(solution([9, 3, 9, 3, 7, 9, 9]))  # 7
print(solution([2, 2, 2]))  # 2
print(solution([2, 2, 3]))  # 3
