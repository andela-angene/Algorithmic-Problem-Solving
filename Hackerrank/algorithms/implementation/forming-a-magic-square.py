from itertools import permutations


def generate_order_3_magic_squars():
    checks = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (2, 4, 6), (0, 4, 8)
    ]
    magic_squares = []

    for i in permutations([1, 2, 3, 4, 5, 6, 7, 8, 9]):
        is_magic = True
        first = checks[0]
        num = i[first[0]] + i[first[1]] + i[first[2]]
        for x in checks:
            if i[x[0]] + i[x[1]] + i[x[2]] != num:
                is_magic = False
                break
        if is_magic:
            magic_squares.append(i)

    return magic_squares


a = [(2, 7, 6, 9, 5, 1, 4, 3, 8), (2, 9, 4, 7, 5, 3, 6, 1, 8),
     (4, 3, 8, 9, 5, 1, 2, 7, 6), (4, 9, 2, 3, 5, 7, 8, 1, 6),
     (6, 1, 8, 7, 5, 3, 2, 9, 4), (6, 7, 2, 1, 5, 9, 8, 3, 4),
     (8, 1, 6, 3, 5, 7, 4, 9, 2), (8, 3, 4, 1, 5, 9, 6, 7, 2)]


source = [4, 8, 2, 4, 5, 7, 6, 1, 6]
# source = [4, 9, 2, 3, 5, 7, 8, 1, 5]

min_removal = float('inf')
for i in a:
    to_remove = [abs(x - y) for x, y in zip(source, i) if x != y]
    min_removal = min(min_removal, sum(to_remove))

print(min_removal)

