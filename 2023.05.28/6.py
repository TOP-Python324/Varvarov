# ПЕРЕИМЕНОВАТЬ: клетка (игрового) поля — square, field
digit, digit1 = input(), input()

if (-1 <= ord(digit[0]) - ord(digit1[0]) <= 1) and (-1 <= int(digit[1]) - int(digit1[1]) <= 1):
    print('ДА')
else:
    print('НЕТ')


# d4
# c3
# ДА

# f7
# b5
# НЕТ


