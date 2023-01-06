from pathlib import Path
from view import fnd_cont

d = Path('tel_book.txt')
d_csv = Path('tel_book.csv')


def write_data(person_data):
    with open(d, 'a') as data:
        a = f'{person_data} \n'
        data.write(a)

def find_contact():
    res = fnd_cont()
    with open(d, 'r') as data:
        temp = data.readlines()
        for i in range (len(temp)):
            if res in temp[i]:
                return temp[i]

def change_contact():
    res = fnd_cont()
    res_data = []
    with open(d, 'r') as data:
        temp = data.readlines()
        for i in range (len(temp)):
            if res in temp[i]:
                continue
            res_data.append(temp[i])
    with open(d, 'w') as data:
        data.write(''.join(res_data))
        print('/nКонтакт удален!/n')

def read_contact():
    with open(d, 'r') as data:
        return data.read()

def import_file():
    f_name = fnd_cont()
    with open(f_name, 'r') as data:
        temp = data.read()
    main_data = read_contact()
    res = main_data+temp.replace(';', ' ')
    with open(d, 'w') as data:
            data.write(res)
    print('\nИмпортирование завершено\n')
    return res