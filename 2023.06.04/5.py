telegram_text = input()
price = 30

for _ in telegram_text:
    if len(telegram_text) > 0:
        cost = len(''.join(telegram_text.split())) * price
print()
print(f'{cost // 100} руб. {cost % 100} коп.')

# ждите скоро прибудет новая партия товара

# 10 руб. 50 коп.