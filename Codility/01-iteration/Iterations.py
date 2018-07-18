def binary_gap_v0(num):
    num = str(bin(num)[2:])
    max_len = 0
    current_len = 0
    gate_open = False
    counter = 0

    while counter < len(num) - 1:
        value = num[counter]
        next_value = num[counter + 1]
        if value == '1' and next_value == '0':
            gate_open = True
        if value == '0':
            if gate_open:
                current_len += 1
            if next_value == '1':
                gate_open = False
                max_len = max(current_len, max_len)
                current_len = 0
        counter += 1

    return max_len


def binary_gap(num):
    num, is_gate_open = str(bin(num)[2:]), False
    max_zeros_len = consecutive_zeros = 0

    for i in range(len(num) - 1):
        value, next_value = num[i], num[i + 1]
        if value == '1' and next_value == '0':
            is_gate_open = True
        if value == '0':
            if is_gate_open:
                consecutive_zeros += 1
            if next_value == '1':
                max_zeros_len = max(consecutive_zeros, max_zeros_len)
                is_gate_open, consecutive_zeros = False, 0

    return max_zeros_len

print(binary_gap(15))
print(binary_gap(1041))
print(binary_gap(0))
print(binary_gap(9))
