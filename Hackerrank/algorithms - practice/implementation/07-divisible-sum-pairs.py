def divisible(n, k, ar):
    result = 0

    for i in range(0, n - 1):
        for j in range(i + 1, n):
            if (ar[i] + ar[j]) % k == 0:
                result += 1

    return result


print(divisible(6, 3, [1, 3, 2, 6, 1, 2]))
print(divisible(3, 3, [1, 3, 2]))
print(divisible(1, 3, [1]))
