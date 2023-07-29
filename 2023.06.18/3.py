def numbers_strip(numbers=[float], n=1, *, copy=False):
    for _ in range(n):
        numbers.remove(min(numbers))
        numbers.remove(max(numbers))
    return numbers.copy() if copy else numbers

# >>> numbers = [1, 2, 3, 4, 5]
# >>> lis_n = numbers_strip(numbers)
# >>> lis_n
# [2, 3, 4]
# >>> numbers is lis_n
# True
# >>> numbers = [10, 20, 30, 40, 50, 60]
# >>> lis_n = numbers_strip(numbers, 2, copy=True)
# >>> lis_n
# [30, 40]
# >>> numbers is lis_n
# False