n = int(input())
number_fb1 = 1
number_fb2 = 0
# sum_fb = 0
print()

for _ in range(n):
    # number_fb1 = number_fb2
    # number_fb2 = sum_fb
    # sum_fb = number_fb1 + number_fb2
    # ИСПОЛЬЗОВАТЬ: в Python есть намного более удобный способ обмена значениями двух переменных, без привлечения третьей:
    number_fb1, number_fb2 = number_fb2, number_fb1 + number_fb2
    print(number_fb2, end=' ')


# 19

# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181


# ИТОГ: очень хорошо — 3/3
