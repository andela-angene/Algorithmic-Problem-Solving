# n = int(input().strip())
# arr = list(input().strip().split(' '))

def insertion(arr):
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

    return arr

def insertion_sort(arr):
    arr = list(map(str, arr))
    arr_len = len(arr)
    counter = 2

    while counter <= arr_len:
        sorted_part = insertion(arr[:counter])
        arr = sorted_part + arr[counter:]
        print(' '.join(arr))
        counter += 1

    return arr

insertion_sort([6, 3, 2, 1, 7, 9, 10, 4])
insertion_sort([6, 2])
insertion_sort([1, 4, 3, 5, 6, 2])

