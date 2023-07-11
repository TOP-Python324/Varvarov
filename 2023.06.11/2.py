fruits_list = []
while True:
    fruits = input()
    fruits_list.append(fruits)
    if len(fruits) >= 1:
        fruits_list
    else:
        fruits == ''
        break
print(*fruits_list[:-3], ' и '.join(fruits_list[-3:-1]), sep=', ')

# 1:банан

# 1:банан

# 2:банан
   # кокос

# 2:банан и кокос

# 3:банан
   # кокос
   # клубника

# 3:банан, кокос и клубника

# 4:банан
   # кокос
   # клубника
   # манго

# 4:банан, кокос, клубника и манго