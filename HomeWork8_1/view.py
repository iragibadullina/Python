def show_menu() -> int:
    print("\n" + "=" * 20)
    print("Выберите необходимое действие")
    print("1. Найти сотрудника")
    print("2. Сделать выборку сотрудников по должности")
    print("3. Сделать выборку сотрудников по зарплате")
    print("4. Добавить сотрудника")
    print("5. Удалить сотрудника")
    print("6. Обновить данные сотрудника")
    print("7. Экспортировать данные в формате json")
    print("8. Экспортировать данные в формате cmv")
    print("9. Закончить работу")
    choice  = int(input("Введите номер необходимого действия: "))
    return choice

def print_result(data: list):
    for el in data:
        s = ''
        for v, k in el.items():
            s += f'{v}: {k}\n'
        print(s)

def get_search_name() -> str:
    return input('Введите фамилию для поиска: ')

def get_new_user() -> str:
    id = input('Введите id: ')
    last_name = input('Введите фымилию: ')
    first_name = input('Введите имя: ')
    phone_number = input('Введите номер телефона: ')
    position = input('Введите должность: ')
    salary = input('Введите зарплату: ')
    return f'{id};{last_name};{first_name};{phone_number};{position};{salary}'

def get_file_name() -> str:
    return input('Введите название файла для сохранения: ')

def get_search_position() -> str:
    return input('Введите должность для поиска: ')

def get_search_salary() -> str:
    return input('Введите зарплату для поиска: ')

def get_add_user() -> str:
    return input('Введите данные нового сотрудника: ')

