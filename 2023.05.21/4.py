num = int(input())

c = num % 10
x = num // 10 % 10
z = num // 100

amount = f'Сумма цифр = {z + x + c}'
comp = f'Произведение цифр =  {z * x * c}'

print(amount)
print(comp)

# 369
# Сумма цифр = 18
# Произведение цифр =  162