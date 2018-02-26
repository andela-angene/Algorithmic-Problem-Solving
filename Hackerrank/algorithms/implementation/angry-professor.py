def angryProfessor(k, a):
    n = 0
    for i in a:
        if i <= 0:
            n += 1
    print('YES' if n < k else 'NO')



angryProfessor(3, [-1, -3, 4, 2])
angryProfessor(2, [0, -1, 2, 1])
