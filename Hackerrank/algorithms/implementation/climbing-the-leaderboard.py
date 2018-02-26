import bisect

leader_board = [100, 100, 50, 40, 40, 20, 10]
scores = [5, 25, 50, 120]

lead_values = [1]
position = 1
for i in range(1, len(leader_board)):
    position = position if leader_board[i] == leader_board[i - 1] \
        else position + 1
    lead_values.append(position)

lead_values.append(position + 1)
leader_board.reverse()
lead_values.reverse()
for i in scores:
    index = bisect.bisect_right(leader_board, i)
    print(lead_values[index])
