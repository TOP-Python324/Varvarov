numb, numb1 = int(input()), int(input())

print(f'{numb} делится на {numb1} нацело \n'
      f'частное: {numb // numb1}\n')


# 44
# 11
# 44 делится на 11 нацело
# частное: 4

num, num1 = int(input()), int(input())

print(f'{num} не делиться на {num1} нацело \n'
      f'неполное частное: {num // num1} \n'
      f'остаток: {num % num1}')
         

# 49
# 5
# 49 не делиться на 5 нацело
# неполное частное: 9
# остаток: 4


# КОММЕНТАРИЙ: вот здесь вижу, что действительно пытались решить самостоятельно...

# КОММЕНТАРИЙ: обращаемся к тексту задания:
#  "программа получает из stdin два числа" — два числа за один запуск, не четыре
#  пользователь может ввести любую пару чисел, верно? и если для вашего кода пользователь введёт, например 10 и 7 — то ваша программа выдаст неверный ответ
#  тема задания: условные конструкции — чем мы и занимались на лекции — отсюда как раз и следует, что вам необходимо выяснить касательно введённых чисел: делятся они друг на друга нацело или нет? а дальше — в зависимости от результата — выполнить ЛИБО одно действие, ЛИБО другое


# ИТОГ: переделать — 1/5
