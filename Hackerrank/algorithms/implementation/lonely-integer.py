catch = [0] * 100
n = 5
ar = [0, 0, 1, 2, 1]
for i in ar:
    catch[i] += 1

for i in range(1, len(catch)):
    if catch[i] not in [0, 2]:
        print(i)
        break

