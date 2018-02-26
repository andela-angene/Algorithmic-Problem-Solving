def solution(A):
    total = sum(A)
    current_sum = A[0]
    min_diff = None

    for i in range(1, len(A)):
        difference = abs((total - current_sum) - current_sum)

        if (min_diff is None) or difference < min_diff:
            min_diff = difference
        current_sum += A[i]

    return min_diff


print(solution([3, 1, 2, 4, 3]))  # 1
print(solution([2, 4]))  # 2
print(solution([3, 8, 10]))  # 1
print(solution([-1, 2, -3]))  # 1
print(solution([0, 0, 0]))  # 1
