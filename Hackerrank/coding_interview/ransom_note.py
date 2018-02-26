#!/bin/python3

import sys
test_data = []
with open('data/ransom_note.txt') as data:
    for line in data:
        test_data.append(line.strip())


def ransom_note(magazine, ransom):
    magazine_words = {}
    ransom_words = {}

    for word in magazine:
        if word in magazine_words:
            magazine_words[word] += 1
        else:
            magazine_words[word] = 1

    for word in ransom:
        if word not in magazine_words:
            return False
        if word in ransom_words:
            ransom_words[word] += 1
            if ransom_words[word] > magazine_words[word]:
                return False
        else:
            ransom_words[word] = 1

    return True


print(ransom_note(['a', 'b'], ['c']))
print(ransom_note(['a', 'b'], ['b']))

m, n = map(int, test_data[0].strip().split(' '))
magazine = test_data[1].strip().split(' ')
ransom = test_data[2].strip().split(' ')
answer = ransom_note(magazine, ransom)
if (answer):
    print("Yes")
else:
    print("No")
