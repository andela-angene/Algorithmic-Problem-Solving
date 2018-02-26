def count_substring(string, sub_string):
    count, index = 0, 0
    while index != -1:
        index = string.find(sub_string, index)
        if index != -1:
            count += 1
            index += 1
    return count


print(count_substring('ABCDCDC', 'CDC'))
