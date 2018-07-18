def append_and_del(short_str, long_str, k):
    if len(long_str) < len(short_str):
        short_str, long_str = long_str, short_str
    len_short, len_long = len(short_str), len(long_str)
    split_index = len_short
    for i in range(len_short):
        if short_str[i] != long_str[i]:
            split_index = i
            break
    min_req = (len_short - split_index) + (len_long - split_index)
    if k > (len_long + len_short):
        return 'Yes'
    if k >= min_req and (k - min_req) % 2 == 0:
        return 'Yes'
    return 'No'


print(append_and_del('hackerhappy', 'hackerrank', 9))  # y
print(append_and_del('hackerhappy', 'hackerrank', 10))  # n
print(append_and_del('hacker', 'hacah', 11))  # y
print(append_and_del('aba', 'aba', 5))  # n
print(append_and_del('aba', 'aba', 7))  # y
print(append_and_del('qwerasdf', 'qwerbsdf', 6))  # n
print(append_and_del('aaaaaaaaaa', 'aaaaa', 7))  # y
print(append_and_del('abc', 'abcd', 1))  # y
