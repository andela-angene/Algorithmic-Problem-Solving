def choco(n, data, day, month):
    bars = 0
    i = 0
    while i <= n - month:
        if sum(data[i:i + month]) == day:
            bars += 1
        i += 1

    return bars


print(choco(1, [4], 4, 1))  # 1
print(choco(5, [1, 2, 1, 3, 2], 3, 2))  # 2
print(choco(6, [1, 1, 1, 1, 1, 1], 3, 2))  # 0
