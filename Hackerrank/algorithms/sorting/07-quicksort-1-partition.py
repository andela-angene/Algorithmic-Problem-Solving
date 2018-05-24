n, l, left, right = input(), [i for i in input().strip().split()], [], []
el, equal = int(l[0]), [l[0]]

for i in range(1, len(l)):
    if int(l[i]) == el:
        equal.append(l[i])
    elif int(l[i]) > el:
        right.append(l[i])
    else:
        left.append(l[i])

print(' '.join(left + equal + right))
