def check_t(t_string):
    for i in range(len(t_string) - 2):
        if t_string[i] != t_string[i + 2]:
            return False
    return True


def two_chars(n, text):
    chars, lens = [], []

    for char in text:
        if char not in chars:
            chars.append(char)

    len_chars = len(chars)
    for i in range(len_chars - 1):
        for j in range(i + 1, len_chars):
            t_string = str(text)
            for char in chars:
                if char not in [chars[i], chars[j]]:
                    t_string = t_string.replace(char, '')
            if check_t(t_string):
                lens.append(len(t_string))

    return 0 if len(lens) == 0 else max(lens)


print(two_chars(10, 'beabeefeab'))
print(two_chars(375,
                'uyetuppelecblwipdsqabzsvyfaezeqhpnalahnpkdbhzjglcuqfjnzpmbwprelbayyzovkhacgrglrdpmvaexkgertilnfooeazvulykxypsxicofnbyivkthovpjzhpohdhuebazlukfhaavfsssuupbyjqdxwwqlicbjirirspqhxomjdzswtsogugmbnslcalcfaxqmionsxdgpkotffycphsewyqvhqcwlufekxwoiudxjixchfqlavjwhaennkmfsdhigyeifnoskjbzgzggsmshdhzagpznkbahixqgrdnmlzogprctjggsujmqzqknvcuvdinesbwpirfasnvfjqceyrkknyvdritcfyowsgfrevzon'))
