# Домашнее задание Семинар 6
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# .
# Структура данных:
# Фамилия, имя, отчество, номер телефона.
# .
# Пример данных:
# Ivanov, Ivan, Ivanovich, +79111234567
# Petrov, Petr, Petrovich, +79119876543
# .
# Функции справочника:
# - Показать все записи
# - Найти запись по вхождению частей имени
# - Найти запись по телефону
# - Добавить новый контакт
# - Удалить контакт
# - Изменить номер телефона у контакта
# .
# Пример работы программы:
# .
# При запуске программы пользователю выдается меню:

# Введите номер действия:
# 1 - Показать все записи
# 2 - Найти запись по вхождению частей имени
# 3 - Найти запись по телефону
# 4 - Добавить новый контакт
# 5 - Удалить контакт
# 6 - Изменить номер телефона у контакта
# 7 - Выход

import os
directFile = "teldirect.txt"

def DataOutput():      # функция вывода данных
    os.system("cls")
    print('Данные справочника:')
    with open(directFile, 'r', encoding="utf8") as data:
        for line in data:
            withoutStrip = line.strip('\n')
            print(withoutStrip)
    input('Для выхода в основное меню нажмите Enter')

def DataAdding():     # функция добавления данных
    os.system("cls")
    while True:
        print('ДОБАВЛЕНИЕ ДАННЫХ В СПРАВОЧНИК\n'
            '(Нажмите Enter для выхода в основное меню).')
        surname = input('Введите фамилию: ')
        if surname == '':
            return
        name = input('Введите имя: ')
        patronymic = input('Введите отчество: ')
        phone = input('Введите телефон: ')
        dataOfperson = [surname, name, patronymic, phone]
        if '' in dataOfperson:
            return
        record = ", ".join(dataOfperson) + '\n'
        with open(directFile, 'a', encoding="utf8") as data:
            data.write(record)
        print(f'Введенные вами данные: {record}')

def SearchPerson():
    os.system("cls")
    while True:
        txt = input('Введите строку поиска: ')
        if txt == '':
            return
        result = []
        with open(directFile, 'r', encoding="utf8") as data:
            for line in data:
                result.append(line.strip('\n'))
            result = list(filter(lambda line: txt in line, result))
        for printdata in result:
            print(printdata)
        print('Для выхода в основное меню нажмите Enter.')


menu = (f'ТЕЛЕФОННЫЙ СПРАВОЧНИК\n\n'
        'Команды меню\n'
        '1 - Показать все записи\n'
        '2 - Найти запись по вхождению частей имени\n'
        '4 - Добавить новую записи\n')
while True:
    os.system('cls') 
    print(menu)
    command = input('Введите команду: ')
    match command:
        case '1':
            DataOutput()
        case '2':
            SearchPerson()
        case '4':
            DataAdding()





