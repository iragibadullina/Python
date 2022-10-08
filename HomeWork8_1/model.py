import csv
import json

def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i]. values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def write_csv(filename: str, data: list):
     with open(filename, 'w', encoding='utf-8') as fout:
        for i in range(len(data)):
            s = ''
            for v in data[i]. values():
                s += v + ','
            fout.write(f'{s[:-1]}\n')

def read_csv(filename: str) -> list:
    data = []
    fields = ["id","Фамилия","Имя","Номер телефона","Должность","Зарплата"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields,line.strip().split(',')))
            data.append(record)
    return data

def find_by_name(data: list, last_name: str) -> str:
    for el in data:
        if el.get('Фамилия') == last_name:
           return f'{el.get("id")},{el.get("Имя")}, {el.get("Номер телефона")},{el.get("Должность")},{el.get("Зарплата")}'
    return "Такой сотрудник отсутствует"

def add_user(data: list, user_data: str):
    fields = ['id','Фамилия','Имя','Номер телефона','Должность','Зарплата']
    record = dict(zip(fields, user_data.split(',')))
    data.append(record)

def find_by_position(data: list, position: str) -> str:
    for el in data:
        if el.get('Должность') == position:
            return f'{el.get("id")},{el.get("Фамилия")},{el.get("Имя")}, {el.get("Номер телефона")},{el.get("Зарплата")}'
    return "Такой сотрудник отсутствует"

def find_by_salary(data: list, salary: str) -> str:
    for el in data:
        if el.get('Зарплата') == salary:
            return f'{el.get("id")},{el.get("Фамилия")},{el.get("Имя")}, {el.get("Номер телефона")},{el.get("Должность")}'
    return "Такой сотрудник отсутствует"

def delete_by_name(data: list, user_data: str) -> str:
    list = input('Введите данные для удаления: ')
    new_list = list.clear()
    record = dict(zip(new_list, user_data.split(',')))
    data.append(record)


def export_to_json(data: list[list[str]], filename_json):
    mydata = {}
    with open(data, encoding= 'utf-8') as csvfile:
        csvRead = csv.Dictreader(csvfile)
        for rows in csvRead:
            myKey = rows['No']
            data[myKey] = rows
    with open(filename_json, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dums(data))
    return data










