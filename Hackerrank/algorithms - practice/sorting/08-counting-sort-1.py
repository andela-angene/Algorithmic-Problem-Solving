n, ar = int(input()), [int(i) for i in input().strip().split()]
counter = [0] * 100

for i in ar:
    counter[i] += 1

print(' '.join(map(str, counter)))
