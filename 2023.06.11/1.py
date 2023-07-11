email_address = input()

if email_address.count('@') == 1 and email_address.count('.') >= 1:
    print('ДА')
else:
    print('НЕТ')

# foeduvd@ya.ru
# ДА

# yefeorf@iferf
# НЕТ