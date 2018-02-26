# def max_double_slice(arr):
#     if len(arr) < 4:
#         return 0
#     current_sum = max(arr[1], arr[2])
#     min_val = min(arr[1], arr[2])
#     check_min = True
#     max_sum = current_sum
#
#     for i in range(3, len(arr) - 1):
#         element = arr[i]
#         if check_min:
#             if element < min_val:
#                 current_sum += min_val
#                 min_val = element
#             elif element > current_sum + element:
#                 current_sum = element
#                 check_min = False
#             else:
#                 current_sum += element
#         elif current_sum >= current_sum + element:
#             min_val = element
#             check_min = True
#         else:
#             current_sum += element
#
#         if current_sum > max_sum:
#             max_sum = current_sum
#
#     return max_sum if max_sum > 0 else 0


def max_double_slice(arr):
    length = len(arr)
    if length < 4:
        return 0
    current_sum = arr[1]
    max_arr = [0, current_sum]
    max_sum = max([0, current_sum])
    minimum = min(arr[1:-1])

    for i in range(2, length - 1):
        element = arr[i]
        current_sum = max(element, element + current_sum)
        max_sum = max([max_sum, current_sum])
        max_arr.append(current_sum)
    if minimum > 0:
        max_sum -= minimum

    current_sum = arr[length - 2]
    prev = current_sum
    for i in range(length - 3, 0, -1):
        element = arr[i]
        current_sum = max(element, element + current_sum)
        max_sum = max([max_sum, max_arr[i - 1] + prev])
        prev = current_sum

    return max_sum


print(max_double_slice([20, 2, 1, -3, -5, -2, 10, -2, 12, 10]))
print(max_double_slice([0, 10, -5, -2, 0]))  # 10
print(max_double_slice([5, 17, 0, 3]))  # 17

#
print(max_double_slice([3, 2, 6, -1, 4, 5, -1, 2]))  # 17
print(max_double_slice([1, 2, -3, 4, 4]))  # 6
print(max_double_slice([1, 2, -3]))  # 0
print(max_double_slice([20, 2, 1, -3, -5, -2, 10, -2, 12, 10]))  # 22
print(max_double_slice([1, -1, 1, -1, -1, 1, 1, 0, 1]))  # 2
print(max_double_slice([-3, -2, -4, -5]))  # 0
print(max_double_slice([-3, 2, 3, 3, -5]))  # 6
