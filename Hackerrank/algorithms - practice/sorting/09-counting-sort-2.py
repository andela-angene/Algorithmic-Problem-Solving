n, ar = int(input()), [int(i) for i in input().strip().split()]
counter = [0] * 100
# ar = [3, 2]
for i in ar:
    counter[i] += 1

for i in range(100):
    n = 0
    while n < counter[i]:
        print(i, end=' ')
        n += 1
