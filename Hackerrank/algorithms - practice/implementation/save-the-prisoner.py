prisoners, sweets, start = 5, 7, 3  # 4


to_first = sweets - (prisoners - start + 1)

print(to_first % prisoners)
