# n = int(input().strip())
# arr = list(input().strip().split(' '))

def insertion1_sort(arr):
    # arr = list(map(str, arr))
    counter = len(arr) - 1
    tobesorted = arr[counter]

    while counter >= 0:
        if counter == 0:
            arr[0] = tobesorted
            counter -= 1
        elif int(tobesorted) >= int(arr[counter - 1]):
            arr[counter] = tobesorted
            counter = -1
        else:
            arr[counter] = arr[counter - 1]
        counter -= 1
        print(' '.join(arr))

    return arr

print(insertion1_sort(['2', '4', '6', '8', '3']))
print(insertion1_sort([2, 4, 6, 8, 1]))
print(insertion1_sort([2, 4, 6, 8, 20]))
print(insertion1_sort([2]))
print(insertion1_sort([2, 1]))
