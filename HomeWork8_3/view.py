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
    return int(input("Введите номер необходимого действия: "))
   
def show_search_menu() -> int:
    print("\n" + "=" * 20)
    print ("1. Найти сотрудника по индификатору")
    print ("2. Найти сотрудника по фамилии")
    print ("3. Найти сотрудника по номеру телефона")
    return int(input("Выберите действие: "))

def show_update_menu() ->int:
    print("\n" + "=" * 20)
    print ("1. Обновить данные сотрудника по индификатору")
    print ("2. Обновит данные сотрудника по фамилии")
    return int(input("Выберите действие: "))

def get_id() -> int:
    return int(input("Введите индификатор сотрудника: "))

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

def get_salary_range() -> tuple:
    lo = float(input("Введите начало диапазона знвчений: "))
    hi = float(input("Введите конец диапазона знвчений: "))
    return lo, hi

def get_employee() -> dict:
    result = {}
    result["id"] = get_id()
    result["last_name"] = get_last_name()
    result["first_name"] = get_first_name()
    result["position"] = get_position() 
    result["phone_number"] = get_phone_number() 
    result["salary"] = get_salary() 
    return result
    
def get_changes() ->int:
    print("\n выберите данные, которые необходимо изменит: ")
    print("1. Индетификатор")
    print("2. Фамилия")
    print("3. Имя")
    print("4. Должность")
    print("5. Телефон")
    print("6. Зарплата")
    return int(input("Введите номер пункта: "))

def no_employee_error():
    print("Такого сотрудника нет")

def show_employee_info(employee: dict):
    for k, v in employee.items():
        print(f'{k}:{v}')
