def hacker_rank(text):
    hackrank = list('hackerrank')
    for c in text:
        if c == hackrank[0]:
            hackrank.remove(c)
            if len(hackrank) == 0:
                return 'YES'

    return 'NO'


print(hacker_rank('hereiamstackerrank'))
print(hacker_rank('hackerworld'))
