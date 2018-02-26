# nums = [4, 6, 5, 3, 3, 1] # 3

#nums = [1, 2, 2, 3, 1, 2] # 5
nums = "7 12 13 19 17 7 3 18 9 18 13 12 3 13 7 9 18 9 18 9 13 18 13 13 18 18 17 17 13 3 12 13 19 17 19 12 18 13 7 3 3 12 7 13 7 3 17 9 13 13 13 12 18 18 9 7 19 17 13 18 19 9 18 18 18 19 17 7 12 3 13 19 12 3 9 17 13 19 12 18 13 18 18 18 17 13 3 18 19 7 12 9 18 3 13 13 9 7"
nums = [int(i) for i in nums.split()]

unique_nums, result = set(nums), 0

for num in unique_nums:
    total_p = 0
    total_n = 0
    for i in nums:
        if num - i in [1, 0]:
            total_p += 1
        elif num - i in [-1, 0]:
            total_n += 1
    result = max(result, total_p, total_n)

print(result)

