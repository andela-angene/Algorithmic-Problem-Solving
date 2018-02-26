import math


def count_factors(N):
    if N == 1:
        return 1
    square_root = math.sqrt(N)
    factors = 1 if square_root % 1 == 0 else 2
    limit = math.floor(square_root)
    counter = 2
    while counter <= limit:
        if (N / float(counter)) % 1 == 0:
            factors += 2
        counter += 1

    return factors


print(count_factors(2))
print(count_factors(24))
print(count_factors(25))
