n = 6
numbers = [7, 1, 3, 4, 1, 7]
table, minimum = {}, float('inf')
for i in range(n):
	item = numbers[i]
	if item in table:
		minimum = min(minimum, i - table[item])
	table[item] = i

print(minimum if minimum != float('inf') else -1)

