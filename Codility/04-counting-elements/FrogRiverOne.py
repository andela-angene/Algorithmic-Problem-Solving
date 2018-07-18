# FrogRiverOne


def solution(x, A):
    counter = 0
    leaves = [0] * x

    for i in range(0, len(A)):
        item = A[i]
        if item <= x and item != leaves[item - 1]:
            leaves[item - 1] = item
            counter += 1
            if counter == x:
                return i

    return -1


# (100%) https://codility.com/demo/results/training99662N-CZ7/

print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))  # 6
print(solution(8, [1, 2, 3]))  # -1
print(solution(4, [4, 2, 4, 1, 3, 5]))  # 4
print(solution(1, [1]))  # 0
print(solution(1, [2]))  # 0
