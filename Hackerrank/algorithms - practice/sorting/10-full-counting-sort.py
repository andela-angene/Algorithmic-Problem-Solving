import sys

data = []
with open('data/10-full-counting-sort.txt') as file:
    for line in file:
        data.append(line.strip())


n, ar, counter = int(data[0].strip()), [], {}
half = n/2

for i in range(n):
    item = data[1:][i].split()
    ar.append(item)

    item_count = item[0]
    if item_count in counter:
        counter[item_count].append(i)
    else:
        counter[item_count] = [i]

for i in range(100):
    if str(i) in counter:
        item = counter[str(i)]
        for j in item:
            print(ar[j][1] if j >= half else '-', end=' ')
