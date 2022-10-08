from view import(show_menu, print_result, get_search_name, get_search_position, get_salary_range, get_new_user, get_file_name)
from models import (write_txt, write_csv, read_csv, find_by_name, find_by_position,find_by_salary_range, add_user,read_json)

def work_with_database():
    choice = show_menu()
    d_base = read_csv('db.csv')

    while(choice !=6):
        if choice == 0:
            print_result(d_base)
        elif choice == 1:
            name = get_search_name()
            print(find_by_name(d_base, name))
        elif choice == 2:
            position = get_search_position()
            print(find_by_position(d_base, position))
        elif choice == 3:
            salary = get_salary_range()
            print(find_by_salary_range(d_base, salary))
        elif choice == 4:
            user_data = get_new_user()
            add_user(d_base, user_data)
            write_csv('db.csv', d_base)
       
        

        elif choice == 6:
            file_name = get_file_name()
            write_txt(file_name, d_base)
        choice = show_menu()

