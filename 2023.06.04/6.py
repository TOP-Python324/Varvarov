ticket = input()
# КОММЕНТАРИЙ: есть ещё срезы и встроенная функция sum()
ticket_number1 = int(ticket[0]) + int(ticket[1]) + int(ticket[2])
ticket_number2 = int(ticket[3]) + int(ticket[4]) + int(ticket[5])
if ticket_number1 == ticket_number2:
    print('ДА')
else:
    print('НЕТ')


# 264516
# ДА

# 754972
# НЕТ


# ИТОГ: очень хорошо — 2/2
