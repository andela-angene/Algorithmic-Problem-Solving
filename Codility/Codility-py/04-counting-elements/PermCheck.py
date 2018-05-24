# PermCheck


def solution(a):
    a.sort()
    for i in range(1, len(a) + 1):
        if i != a[i - 1]:
            return 0

    return 1


# (100%) https://codility.com/demo/results/trainingX98HWU-GHV/

print(solution([4, 1, 3, 2]))  # 1
print(solution([4, 1, 3]))  # 0
