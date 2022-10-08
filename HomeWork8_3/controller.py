from view import (get_employee,get_changes,get_id, get_first_name, get_last_name,
                get_phone_number, get_position,get_salary,get_salary_range,show_menu,
                show_search_menu,show_update_menu,no_employee_error,show_employee_info)

from model import(read_csv,read_json,write_csv,write_json,find_employee_by_id,
                find_employee_by_last_name,find_employee_by_phone_number,
                find_employee_by_salary_range, update_employee,add_employee,
                del_employee,find_employee,find_employee_by_position)  

def work_with_database():  
    employees = read_csv()
    employee = {} 
    while True:
        choice = show_menu()
        if choice == 1:
            employee = find_employee(employees)
            if employee is None:
                no_employee_error() 
            else:
                show_employee_info(employees) 
        elif choice == 2:
            position = input("Введите название позиции: ")
            emp_by_position = find_employee_by_position(employee, position) 
            if not emp_by_position:
                no_employee_error()
            else:
                for emp in emp_by_position:
                    show_employee_info(emp)
        elif choice == 3:
            emp_by_salary = find_employee_by_salary_range(employee) 
            if not emp_by_salary:
                no_employee_error()
            else:
                for emp in emp_by_salary:
                    show_employee_info(emp)
        elif choice == 4:
            add_employee(employees)
        elif choice == 5:
            fired_employee = get_employee()
            del_employee(employees, fired_employee)
        elif choice == 6:
            employee = find_employee(employees)
            update_employee(employees, employee)
        elif choice == 7:
            write_json(employees)
        elif choice == 8:
            write_csv(employees)
        elif choice == 9:
            write_csv(employees)

            break
