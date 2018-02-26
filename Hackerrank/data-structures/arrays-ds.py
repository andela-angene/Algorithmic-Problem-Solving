n = 4
arr = [int(arr_temp) for arr_temp in '2 3 4 1'.strip().split(' ')]

collect = ''
for i in range(n):
    collect += str(arr[n - 1 - i]) + ' '

print(collect)
