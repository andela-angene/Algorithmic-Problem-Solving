def kangaroo(x1, v1, x2, v2):
    if v1 == v2:
        return 'YES' if x1 == x2 else 'NO'
    distance = (v2 * x1 - v1 * x2) / (v2 - v1)

    if distance < min(x1, x2) or distance % 1 != 0 or ((distance - x1) / v1) % 1 != 0:
        return 'NO'
    return 'YES'

print(kangaroo(0, 3, 4, 2))
print(kangaroo(0, 2, 5, 3))
print(kangaroo(0, 5, 1, 3))
print(kangaroo(0, 2, 1, 2))
print(kangaroo(1, 2, 1, 2))
print(kangaroo(21, 6, 47, 3))
print(kangaroo(35, 1, 45, 3))
