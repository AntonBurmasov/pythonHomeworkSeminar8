
import validate



def main_menu():
    print('---')
    print('Главное меню.')
    mode = input('1. Записать данные в книгу.\n2. Показать всю книгу.\n3. Произвести поиск.\n4.Выход.\nВведите 1, 2,3 или 4.')
    if mode in '1234':
        print('---')
        return int(mode)
    else:
        print('Ошибка! Введите 1, 2, 3 или 4!')


def write_data():
    phone_record = [input('Введите имя: ').title(), input('Введите фамилию: ').title()]
    phone = ''
    while not validate.check_phone(phone):
        phone = input('Введите номер телефона: ')
        if not validate.check_phone(phone):
            print('Телефон введен неверно, попробуйте снова.')
    phone_record.append(phone)
    description = input('Введите описание: ')
    if description:
        phone_record.append(description)
    print(f'Запись внесена в книгу: {str.join(", ", phone_record)}')
    return phone_record

def search_data():
    return input('Введите фамилию для поиска:')

def show_data(data):
    print(f'Найдено записей: {len(data)}\n')
    for line in data:
        print(line)

def show_ext_data(data):
    print(f'Найдено записей: {len(data)}\n')
    for line in data:
        for text in line:
            print(text)

