n = int(input())
number_fb1 = 1
number_fb2 = 1
sum_fb = 0
print()

for _ in range(n):
    number_fb1 = number_fb2
    number_fb2 = sum_fb
    sum_fb = number_fb1 + number_fb2
    print(sum_fb, end=' ')

# 19

# 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181