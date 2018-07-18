def pangram(text):
    text = text.lower()
    for c in 'abcdefghijklmnopqrstuvwxyz':
        if text.find(c) == -1:
            return 'not pangram'
    return 'pangram'


print(pangram('todsf'))
print(pangram('We promptly judged antique ivory buckles for the next prize'))
print(pangram('We promptly judged antique ivory buckles for the prize'))
print(pangram('The quick brown fox jumps over the lazy dog'))
