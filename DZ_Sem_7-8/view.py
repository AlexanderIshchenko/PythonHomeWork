def input_data():
    surname = input('Введите фамилию: ')
    name = input('Введите имя: ')
    tel = input('Введите номер телефона: ')
    return f'{surname} {name} {tel}'

def output_data(personal_data):
    print(f'\n{personal_data}')

def var_funcs():
    print(
    '\nВарианты работы с телефонной книгой:\n'
    '\n'
    '1 - Найти контакт\n2 - Добавить контакт\n3 - Удалить контакт\n4 - Импортировать csv\n'
    )
    var = int(input('Введите номер операции --> '))
    while ((var < 1) or (var > 5)):
        var = int(input('Введите номер операции (1-4) --> '))
    return var

def fnd_cont():
    fnd = input('Введите данные для поиска --> ')
    return fnd



