# aba
# 10


repeated, n = 'aba', 10
remainder = n % len(repeated)

first_as = repeated[:remainder].count('a')
last_as = repeated[remainder:].count('a')

print((first_as + last_as) * (n // len(repeated)) + first_as)
