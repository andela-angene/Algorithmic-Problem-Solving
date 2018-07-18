import math


def solution(N):
    max_num = math.floor(math.sqrt(N))
    min_perimeter = 2 * (N + 1)
    counter = 2

    while counter <= max_num:
        divide = N / float(counter)
        if divide % 1 == 0:
            perimeter = 2 * (divide + counter)
            min_perimeter = min([min_perimeter, perimeter])
        counter += 1

    return int(min_perimeter)



print(solution(30))
print(solution(1))
print(solution(100))
