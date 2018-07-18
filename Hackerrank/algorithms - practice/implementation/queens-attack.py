square, k = 5, 3
position = (4, 3)
obstacles = {
    1: [1],
    4: [2],
    2: [3, 1]
}

checks = {
    'top': [square],
    'bottom': [1],
    'left': [1],
    'right': [square]
}

for row in obstacles:
    for col in obstacles[row]:
        if row == position[0]:
            if position[1] > col:
                checks['left'].append(col + 1)
            else:
                checks['right'].append(col - 1)
        if col == position[1]:
            if position[0] > row:
                checks['bottom'].append(row + 1)
            else:
                checks['top'].append(row - 1)

straight_sum = (min(checks['top']) - position[0]) +\
               (position[0] - max(checks['bottom'])) +\
               (min(checks['right']) - position[1]) + \
               (position[1] - max(checks['left']))


def get_diagonal_sum(signs):
    d_row, d_col = position
    diagonal = 0
    row_bool = d_row < square if signs[0] else d_row > 1
    col_bool = d_col < square if signs[1] else d_col > 1
    while row_bool and col_bool:
        if signs[0]:
            d_row += 1
            row_bool = d_row < square
        else:
            d_row -= 1
            row_bool = d_row > 1

        if signs[1]:
            d_col += 1
            col_bool = d_col < square
        else:
            d_col -= 1
            col_bool = d_col > 1
        if d_row in obstacles and d_col in obstacles[d_row]:
            break
        diagonal += 1
    return diagonal


print(get_diagonal_sum([True, True]) +
      get_diagonal_sum([False, True]) +
      get_diagonal_sum([True, False]) +
      get_diagonal_sum([False, False]) +
      straight_sum)
