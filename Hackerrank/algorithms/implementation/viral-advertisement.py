# start with 5

days, result, shares = int(input().strip()), 0, 5

for i in range(days):
    success = shares // 2
    result += success
    shares = success * 3

print(result)
