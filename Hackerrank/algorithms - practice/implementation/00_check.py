n = 2
balls = [
    [1, 1],
    [1, 1]
]


def organize_balls(n, balls):
    ball_sums = [0] * n
    container_cap = []

    for items in balls:
        container_cap.append(sum(items))
        for i in range(len(items)):
            ball_sums[i] += items[i]

    possible = sorted(ball_sums) == sorted(container_cap)
    return 'Possible' if possible else 'Impossible'


total = int(input())
for _ in range(total):
    n = int(input())
    balls = []
    for _ in range(n):
        balls.append([int(i) for i in input().split()])

    print(organize_balls(n, balls))
