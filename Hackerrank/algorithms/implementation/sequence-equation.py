nums = [2, 1]
table = {}

for i in range(1, len(nums) + 1):
    table[nums[i - 1]] = i

for i in range(1, len(nums) + 1):
    print(table[table[i]])
