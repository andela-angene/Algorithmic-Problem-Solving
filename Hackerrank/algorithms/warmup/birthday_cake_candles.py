def cake_candles(n, ar):
    tallest = ar[0]
    num = 1

    for candle in ar[1:]:
        if candle > tallest:
            tallest = candle
            num = 1
        elif candle == tallest:
            num += 1

    return num

print(cake_candles(4, [3, 2, 1, 3]))
