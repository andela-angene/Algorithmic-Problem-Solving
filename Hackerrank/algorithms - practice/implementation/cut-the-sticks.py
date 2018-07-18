number_of_sticks = 6
sticks, i = [5, 4, 4, 2, 2, 8], -1
# sticks, i = [1, 2, 3, 4, 3, 3, 2, 1], -1
sticks.sort()

while i < number_of_sticks:
    if number_of_sticks - i - 1 != 0:
        print(number_of_sticks - i - 1)
    i += 1
    while i + 1 < number_of_sticks and sticks[i] == sticks[i + 1]:
        i += 1
