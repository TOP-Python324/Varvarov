numbers_list = []
while True:
    numb = int(input())
    # КОММЕНТАРИЙ: в случаях, когда нельзя допустить попадания в список объекта, не соответствующего условию, добавление в список стоит расположить после проверки условия
    numbers_list.append(numb)
    if numb % 7 != 0:
        break
print()
print(*numbers_list[-2::-1])


# 7
# 14
# 21
# 28
# 35
# 42
# 49
# 56
# 63
# 5

# 63 56 49 42 35 28 21 14 7


# ИТОГ: отлично — 3/3
