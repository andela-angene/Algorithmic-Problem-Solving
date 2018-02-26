def solution(A):
    length = len(A)
    A.sort()

    for i in range(1, length + 1):
        if i != A[i - 1]:
            return i

    return length + 1


print(solution([2, 3, 1, 5]))  # 4
print(solution([]))  # 1
print(solution([2, 5, 4, 3]))  # 1
print(solution([1, 2, 3, 4]))  # 5
print(solution([5, 2, 3, 4]))  # 1
print(solution([1, 3]))  # 2

# (50%, 100%)
