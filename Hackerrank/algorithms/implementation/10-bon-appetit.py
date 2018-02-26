def bon_appetit(n, k, bill, ar):
    correct_bill = (sum(ar) - ar[k]) / 2

    return 'Bon Appetit' if correct_bill == bill else int(
        (bill - correct_bill))


print(bon_appetit(4, 1, 12, [3, 10, 2, 9]))  # 5

print(bon_appetit(4, 1, 7, [3, 10, 2, 9]))
