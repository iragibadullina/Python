from view import(show_menu, print_result, get_search_name,
                get_new_user, get_file_name, get_search_position,get_search_salary)

from model import write_txt, write_csv, read_csv, find_by_name, add_user,find_by_position, find_by_salary,delete_by_name,export_to_json  

def work_with_database():
    choice == show_menu()
    data_base = read_csv('database.csv')

    while(choice != 6):
        if choice == 1:
            print_result(data_base)
        elif choice == 2:
            name = get_search_name
            print(find_by_name(data_base, name))
        elif choice == 3:
            position = get_search_position
            print(find_by_position(data_base, position))
        elif choice == 4:
            salary = get_search_salary
            print(find_by_salary(data_base, salary))

choice = show_menu()
        

