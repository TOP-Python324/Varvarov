scores_letters = {
    1: 'АВЕИНОРСТ',
    2: 'ДКЛМПУ',
    3: 'БГЬЯ',
    4: 'ЙЫ',
    5: 'ЖЗХЦЧ',
    8: 'ФШЭЮ',
    10: 'Щ',
    15: 'Ъ'
}

word = input()
sum_letters = 0
for letters in word.upper():
    for k, v in scores_letters.items():
        if letters in v:
            sum_letters += k
print()
print(sum_letters)

# биоаккумулирование

# 26