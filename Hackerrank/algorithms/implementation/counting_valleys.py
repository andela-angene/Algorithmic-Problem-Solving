# number_of_steps, steps = input(), input().strip()
steps = 'DDUUDDUDUUUD'
prev_step, valleys, cumulative = 0, 0, 0

for step in steps:
    cumulative += 1 if step == 'U' else -1
    print(cumulative, '==')
    if cumulative < 0 and prev_step >= 0:
        valleys += 1
    prev_step = cumulative

print(valleys)
