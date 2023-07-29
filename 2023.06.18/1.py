special_symbol = ',./?\;:_=+)(*&^%$#@!~-| '
letters_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters_low = 'abcdefghijklmnopqrstuvwxyz'
digits = '0123456789'

def strong_password(strong_pass):
    if len(strong_pass) < 8:
        return False
    if not any(digit in digits for digit in strong_pass):
        return False	
    if not any(upper in letters_up for upper in strong_pass):
        return False	
    if not any(lower in letters_low for lower in strong_pass):
        return False
    if not any(symb in special_symbol for symb in strong_pass):
        return False
    else:
        return True

# >>> strong_password('frpffefw#')
# False
# >>> strong_password('Dnfe%^$ood129')
# True