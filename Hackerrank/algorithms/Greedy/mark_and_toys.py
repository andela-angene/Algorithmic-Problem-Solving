number_of_toys, budget = 7, 50
toys = [1, 12, 5, 111, 200, 1000, 10]

toys.sort()
count = 0

while count < len(toys):
    if budget - toys[count] < 0:
        break
    budget -= toys[count]
    count += 1

print(count)
