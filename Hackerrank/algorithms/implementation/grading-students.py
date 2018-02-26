#!/bin/python3

import sys
test_data = []
with open('data/grading-students.txt') as data:
    for line in data:
        test_data.append(line.strip())


def solve(grades):
    result = []
    for grade in grades:
        if grade < 38:
            result.append(grade)
        else:
            next_multiple = grade if grade % 5 == 0 else 5 - grade % 5 + grade
            if next_multiple - grade < 3:
                result.append(next_multiple)
            else:
                result.append(grade)

    return result


n = int(test_data[0])
grades = []
grades_i = 0
for grades_i in range(n):
    grades_t = int(test_data[grades_i + 1])
    grades.append(grades_t)
result = solve(grades)
print ("\n".join(map(str, result)))
