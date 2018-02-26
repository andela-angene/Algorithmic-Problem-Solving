from collections import defaultdict
# n, m = 4, 5


def max_team(course):
    n, m = len(course), len(course[0])
    table, max_num = defaultdict(int), 0

    for i in range(n):
        i_course = course[i]
        for j in range(i + 1, n):
            j_course, total = course[j], 0
            for z in range(m):
                if i_course[z] == '1' or j_course[z] == '1':
                    total += 1
            table[total] += 1
            max_num = max(total, max_num)

    return max_num, table[max_num]


print(max_team([
    '10101',
    '11100',
    '11010',
    '00101',
]))

print(max_team([
    '101',
    '100',
    '001',
    '000',
]))

print(max_team([
    '1011101',
    '0000000',
    '0100010',
]))

print(max_team([
    '000',
    '000',
    '000',
]))
