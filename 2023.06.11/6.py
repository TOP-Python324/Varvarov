binary_number = set([input()])
prefix_1b = '1b'
prefix_0b = '0b'
prefix_b = 'b'

for binary_numb in binary_number:
    if prefix_1b in binary_numb:
        print('НЕТ')
        break
else:
    prefix_0b in binary_numb and prefix_b in binary_numb
    print('ДА')

# 1b0101010
# НЕТ

# 10101010
# ДА

# 0b01010101
# ДА

# b10101001
# ДА