def max_slice(arr):
    current_sum = arr[0]
    max_sum = current_sum
    max_arr = [max_sum]

    for i in range(1, len(arr)):
        element = arr[i]
        current_sum = max(element, element + current_sum)
        max_sum = max(current_sum, max_sum)
        max_arr.append(max_sum)

    print(max_arr)
    return max_sum

print(max_slice([20, 2, 1, -3, -5, -2, 10, -2, 12, 10]))
