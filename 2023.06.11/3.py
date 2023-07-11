numbers_list1 = [int(list1) for list1 in input().split()]
numbers_list2 = [int(list2) for list2 in input().split()]

if numbers_list1[: len(numbers_list2)] == numbers_list2:
    print('ДА')
else:
    print('НЕТ')

# 1 2 3 4 5 6 7
# 1 2 3 4 5
# ДА

# 1 2 3 4 5 6 7
# 1 2 5
# НЕТ