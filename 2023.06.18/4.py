def countable_nouns(numb: int, year: tuple[str, str, str]):
    if numb % 10 == 1 and numb % 100 != 11:
        return year[0]
    if numb % 10 in (2, 3, 4) and not (numb % 100 in (12, 13, 14)):
        return year[1]
    return year[2]

# >>> countable_nouns(21, ("год", "года", "лет"))
# 'год'
# >>> countable_nouns(4, ("год", "года", "лет"))
# 'года'
# >>> countable_nouns(10, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(13, ("год", "года", "лет"))
# 'лет'
# >>> countable_nouns(24, ("год", "года", "лет"))
# 'года'