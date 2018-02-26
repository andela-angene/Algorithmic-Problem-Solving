from itertools import permutations

s = 'xacxzaa'
b = 'fxaazxacaaxzoecazxaxaz'


def check_permutation(check, item):
    for character in item:
        if character in check:
            check.remove(character)
            item.remove(character)
        else:
            return 0

    return 1


def solution(s, b):
    s = list(s)
    b = list(b)
    limit = len(s)
    counter = 0
    result = 0

    while limit + counter <= len(b):
        result += check_permutation(s, b[counter:(counter + limit)])
        counter += 1

    return result

print(solution(s, b))
