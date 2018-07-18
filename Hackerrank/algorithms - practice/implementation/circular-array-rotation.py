n, rotate, queries = 3, 2, 3
nums = [1, 2, 3]
queries = [0, 1, 2]
rotated = [0]*n

for i in range(n):
    rotated[(i + rotate) % n] = nums[i]

for i in queries:
    print(rotated[i])

