year = int(input())

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
     print('ДА')
else:
     print('НЕТ')
     
# 2400
# ДА

# 2023
# НЕТ