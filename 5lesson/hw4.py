# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def rle_encode(original):
    res = ''
    count = 1

    for i in range(1, len(original)):
        current = original[i]
        prev = original[i-1]
        if current != prev:
            res += f'{count}{prev}'
            count = 1
        else:
            count += 1

        if i == len(original) - 1:
            res += f'{count}{current}'

    return res

def rle_decode(enc):
    res = ''
    current_count_string = ''
    for i in range(len(enc)):
        current = enc[i]
        if current.isdigit():
            current_count_string += current
        else:
            current_count = int(current_count_string)
            current_letter = current
            res += current_letter * current_count
            current_count_string = ''

    return res

input_string = 'AAABFFFTTT'
encoded = rle_encode(input_string)
decoded = rle_decode(encoded)

print(f'{input_string} -> {encoded}')
print(f'{encoded} -> {decoded}')
