n, to_be_removed = 5, 0;
data = ['AAAA', 'BBBBB', 'ABABABAB', 'BABABA', 'AAABBB']

for i in range(n):
    word = data[i]
    prev = word[0]
    for j in range(1, len(word)):
        if word[j] == prev:
            to_be_removed += 1
        prev = word[j]
    print(to_be_removed)
    to_be_removed = 0

