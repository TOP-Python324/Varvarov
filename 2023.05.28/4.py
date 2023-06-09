# ПЕРЕИМЕНОВАТЬ: причём тут цифры? клетка (игрового) поля — square, field
digit = input()
digit1 = input()

if (ord(digit[0]) + int(digit[1])) % 2 == (ord(digit1[0]) + int(digit1[1])) % 2:
    print('ДА')
else:
    print('НЕТ')


# b5
# f7
# ДА


