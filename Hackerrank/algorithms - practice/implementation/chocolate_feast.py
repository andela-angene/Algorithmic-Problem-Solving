# 6 2 2


def chocos(dollars, cost, trade):
    current = total = dollars // cost

    while current // trade > 0:
        wraps = current // trade
        total += wraps
        current = wraps + current % trade

    return total

print(chocos(12, 4, 4))
print(chocos(12, 4, 4))
