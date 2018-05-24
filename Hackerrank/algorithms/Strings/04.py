def char_range(c1, c2):
    for c in range(ord(c1), ord(c2) + 1):
        yield chr(c)


def ceacar_cipher(k, n, text):
    upper = list(char_range('A', 'Z'))
    lower = list(char_range('a', 'z'))
    result = ""

    for i in range(n):
        if text[i].isupper():
            result += upper[(upper.index(text[i]) + k) % 26]
        elif text[i].islower():
            result += lower[(lower.index(text[i]) + k) % 26]
        else:
            result += text[i]

    return result


print(ceacar_cipher(2, 11, 'middle-Outz'))
