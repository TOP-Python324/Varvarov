from random import randrange

n = int(input())

numbers = [
    randrange(1, 10)
    for numb in range(n)
]
print()
print(*numbers, sep='')


# 7

# 1219537


