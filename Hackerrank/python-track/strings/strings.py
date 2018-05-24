def swap_case(s):
    new_str = ''
    for c in s:
        new_str += c.lower() if c.isupper() else c.upper()
    print(s)
