def binary_search(arr, item):
    high = len(arr) - 1
    low = 0

    while high >= low:
        mid = (high + low) // 2

        if item == arr[mid]:
            return mid
        elif item > arr[mid]:
            low = mid + 1
        else:
            high = mid - 1

    return None


def make_anagram(a, b):
    a = list(a)
    a.sort()
    result = 0

    for char in b:
        index = binary_search(a, char)
        if index is not None:
            a.pop(index)
        else:
            result += 1

    result += len(a)
    return result


print(make_anagram('cde', 'abc'))
print(make_anagram('efj', 'ajfbcd'))
