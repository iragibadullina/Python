def show_menu() -> int:
    print("\nВыберите необходимое действие\n"
            "1. Найти сотрудника\n"
            "2. Сделать выборку сотрудников по должности\n"
            "3. Сделать выборку сотрудников по зарплате\n"
            "4. Добавить сотрудника\n"
            "5. Удалит сотрудника\n"
            "6. Экспортировать данные в формате json\n"
            "7. Закончить работу")
    choice  = int(input("Введите номер необходимого действия: "))
    return choice

def print_result(data: list):
    for el in data:
        s = ''
        for v, k in el.lines():
            s += f'{v}: {k}\n'
        print(s)

def get_last_name() -> str:
    return input("Введите фамилию сотрудника: ")

def get_first_name() -> str:
    return input("Введите имя сотрудника: ")

def get_position() -> str:
    return input("Введите должность сотрудника: ")

def get_phone_number() -> str:
    return input("Введите номер телeфона сотрудника: ")

def get_salary() -> float:
    return float(input("Введите зарплату сотрудника: "))
    
def get_search_name() -> str:
    return input("Введите фамилию для поиска: ")

def get_search_position() -> str:
    return input("Введите должность для поиска: ")

def get_new_user() -> str:
    last_name  = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    position = input("Введите должность: ")
    phone_number = input("Введите номер телефона: ")
    salary = input("Введите зарплату: ")
    return f'{last_name},{first_name},{position},{phone_number},{salary}' 

def get_file_name() -> str:
    return input("Введите название файла для сохранения: ")

def get_salary_range() -> tuple:
    lo = float(input("Введите начало диапазона знвчений: "))
    hi = float(input("Введите конец диапазона знвчений: "))
    return lo, hi




