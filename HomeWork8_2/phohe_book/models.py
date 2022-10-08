import csv
import json
from pathlib import Path

def write_txt(filename: str, data: list):
    with open(filename, 'w', encoding='utf-8') as fout:

        for i in range(len(data)):
            s = ''
            for v in data[i].values():
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
    fields = ["Фамилия","Имя","Номер телефона","Описание"]
    with open(filename, 'r', encoding='utf-8') as fin:
        for line in fin:
            record = dict(zip(fields,line.strip().split(',')))
            data.append(record)
    return data

def read_json() -> list:
    data =[]
    with open(Path.cwd() /'db.csv', 'r', encoding='utf-8') as fin:
        for line in fin:
            temp = json.loads(line.strip())
            data.append(list)
    return data

def find_by_name(data: list, last_name: str) -> str:
    for el in data:
        if el.get('Фамилия') == last_name:
           return f'{el.get("Имя")},{el.get("Номер телефона")},{el.get("Должность")},{el.get("Зарплата")}'
    return "Такой сотрудник отсутствует"

def find_by_position(data: list, position: str) -> str:
    for el in data:
        if el.get('Должность') == position:
           return f'{el.get("Фамилия")}, {el.get("Имя")}'
    return "Такой сотрудник отсутствует"

def add_user(data: list, user_data: str):
    fields = ["Фамилия", "Имя","Телефон","Должность","Зарплата"]
    record = dict(zip(fields, user_data.split(',')))
    data.append(record)

def del_user_name(filename: list, data: dict):
    filename.remove(data)

def find_by_salary_range(data: list, salary: int) -> list:
    result = []
    lo, hi = 1000, 5000
    for i in range(len(list)):
        if lo <= len[i] <= hi:
            result.append(data)
    return result