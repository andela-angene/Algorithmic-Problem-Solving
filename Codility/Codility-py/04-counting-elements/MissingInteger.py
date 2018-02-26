# MissingInteger


def solution(a):
    a.sort()
    smallest = 1

    for i in range(0, len(a)):
        if a[i] == smallest:
            smallest += 1

    return smallest


# (100%) https://codility.com/demo/results/trainingEB94WH-98C/

print(solution([1, 3, 6, 4, 1, 2]))  # 5
print(solution([1, 2, 3]))  # 4
print(solution([-1, -2]))  # 1
print(solution([2]))  # 1
print(solution([0]))  # 1
