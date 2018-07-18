word = 'abc'
table = '1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5'.split()

max_height = 0
for c in word:
    max_height = max(int(table[ord(c) - 97]), max_height)

print(max_height * len(word))
