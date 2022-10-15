ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЭЮЯ'*1000000
eu = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'*10000000
mes=input('Введите текст ЗАГЛАВНЫМИ буквами Русского или Английского алфавита: ')
lang=input('Введите язык RU или EU: ')
num=int(input('Введите шаг сдвига '))
d = ''
if lang == 'RU':
    for i in mes:
        place=ru.find(i) 
        new=place+num
        if i in ru:
            d+=ru[new]
        else:
            d+=i
else:
    for i in mes:
        place=eu.find(i) 
        new=place+num
        if i in eu:
            d+=eu[new]
        else:
            d+=i
print(d)