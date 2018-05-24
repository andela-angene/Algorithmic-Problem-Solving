def taum(colors, costs, rate):
    black, white = colors
    b_cost, w_cost = costs
    simple = (black * b_cost) + (white * w_cost)
    to_convert = colors[costs.index(max(costs))]
    rate_factored = (black + white) * (min(w_cost, b_cost)) + to_convert * rate
    return min(simple, rate_factored)

print(taum([3, 6], [9, 1], 1))
print(taum([10, 10], [1, 1], 1))
print(taum([5, 9], [2, 3], 4))
