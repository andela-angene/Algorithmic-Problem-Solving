#!/bin/python3

import sys
test_data = []
with open('data/balanced_brackets.txt') as data:
    for line in data:
        test_data.append(line.strip())


def is_matched(expression):
    brackets = []
    bracket_map = {
        '{': '}',
        '[': ']',
        '(': ')'
    }

    for item in expression:
        if item in ['{', '[', '(']:
            brackets.append(item)
        elif len(brackets) > 0 and item in ['}', ']', ')']:
            check = brackets.pop()
            if bracket_map[check] != item:
                return False
        else:
            return False

    return True if len(brackets) == 0 else False

print(is_matched('{}'))
print(is_matched('}'))
print(is_matched('{'))
print(is_matched('({[]})'))
print(is_matched('({[]])'))

t = int(test_data[0].strip())
for i in range(t):
    expression = test_data[i + 1].strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")

