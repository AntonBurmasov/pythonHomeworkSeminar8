import json

import view


def find_data(data):
    with open('phone_book.csv', 'r', encoding="utf-8") as book:
        data_found = []
        for line in book:
            for text in line.split(';'):
                phone_record = line.split(';')
                phone_record[0] = f'Имя: {phone_record[0]}'
                phone_record[1] = f'Фамилия: {phone_record[1]}'
                phone_record[2] = f'Телефон: {phone_record[2]}'
                if len(phone_record) > 3:
                    phone_record[3] = f'Описание: {phone_record[3]}'
            if data.lower() in phone_record[1].lower():
                data_found.append(phone_record)
        view.show_ext_data(data_found)

def full_output():
    with open('phone_book.csv', 'r', encoding="utf-8") as book:
        data_found = []
        for line in book:
            data_found.append(line.replace(';', ', ').replace('\n', ''))
        view.show_data(data_found)