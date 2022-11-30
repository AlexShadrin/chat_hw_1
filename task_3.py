strs = ['attribute', 'класс', 'функция', 'type']

for s in strs:
    try:
        print(f'Слово "{s}" возможно записать в байтовом типе:', bytes(s, 'ascii'))
    except UnicodeEncodeError:
        print(f'Слово "{s}" невозможно записать в байтовой типе')