alnum, alpha, digit, lowercase, uppercase = [False] * 5
for c in input().strip():
    if c.isalnum():
        alnum = True
    if c.isalpha():
        alpha = True
    if c.isdigit():
        digit = True
    if c.islower():
        lowercase = True
    if c.isupper():
        uppercase = True
for item in [alnum, alpha, digit, lowercase, uppercase]:
    print(item)
