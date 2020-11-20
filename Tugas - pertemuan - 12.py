
kata = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

def terbilang(n):
    if n < 10:
        return kata[n]
    elif n >= 1_000_000_000:
        return terbilang(n // 1_000_000_000) + ' billion ' + (terbilang(n % 1_000_000_000) if n % 1_000_000 != 0 else '')
    elif n >= 1_000_000:
        return terbilang(n // 1_000_000) + ' million ' + (terbilang(n % 1_000_000) if n % 1_000_000 != 0 else '')
    elif n >= 1_000:
        if n // 1_000 == 1:
            return " one thousand " + (terbilang(n % 1_000) if n % 1_000 != 0 else '')
        else:
            return terbilang(n // 1_000) + " thousand " + (terbilang(n % 1_000) if n % 1_000 != 0 else '')
    elif n >= 100:
        if n // 100 == 1:
            return ' one hundred ' + (terbilang(n % 100) if n % 100 != 0 else '')
        else:
            return terbilang(n // 100) + ' hundred ' + (terbilang(n % 100) if n % 100 != 0 else '')
    elif n >= 90:
        return  ' ninety ' + (terbilang(n % 10) if n % 10 != 0 else '')
    elif n >= 80:
        return  ' eighty ' + (terbilang(n % 10) if n % 10 != 0 else '')
    elif n >= 70:
        return  ' seventy ' + (terbilang(n % 10) if n % 10 != 0 else '')
    elif n >= 60:
        return  ' sixty ' + (terbilang(n % 10) if n % 10 != 0 else '')
    elif n >= 50:
        return  ' fifty ' + (terbilang(n % 10) if n % 10 != 0 else '')
    elif n >= 40:
        return  ' forty ' + (terbilang(n % 10) if n % 10 != 0 else '')
    elif n >= 30:
        return  ' thirty ' + (terbilang(n % 10) if n % 10 != 0 else '')
    elif n >= 20:
        return  ' twenty ' + (terbilang(n % 10) if n % 10 != 0 else '')

    else:
        if n == 10:
            return ' ten'
        elif n == 11:
            return ' eleven'
        elif n == 12:
            return 'twelve'
        elif n == 13:
            return 'thirteen'
        elif n == 15:
            return 'fifteen'
        else:
            return terbilang(n % 10) + 'teen'        



import os
while True:
    os.system('cls')
    try:
        n = int(input('input a number ? '))
        print(f'{n:,} = {terbilang(n)}')
        print('='*40)
    except:
        print('wrong input (number only) ...')
    os.system('pause')