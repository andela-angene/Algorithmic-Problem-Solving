def super_reduced_string(s):
    ln = len(s)
    i = 0
    while i < ln - 1:
        if s[i] == s[i + 1]:
            s = s[:i] + s[i + 2:]
            ln = len(s)
            i = -1
        i += 1

    return s if len(s) > 0 else 'Empty String'


print(super_reduced_string('aaabccddd'))
print(super_reduced_string('baab'))
print(super_reduced_string('aa'))
