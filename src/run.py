from system.csv_handler import get_employees, update_employee_file
from system.cli import (create_employee_dataframe,
                        get_target_employee, get_menu_choice,
                        get_employees_dataframe,
                        create_employee,
                        get_selected_employee)
from system.config import EMPLOYEE_LIST_PATH


if __name__ == "__main__":

    employees = get_employees(EMPLOYEE_LIST_PATH)

    while True:
        choice = get_menu_choice()
        print(choice)

        if choice == 1:
            print(get_employees_dataframe(employees))
        
        elif choice == 2:
            target = str(input("Enter full name: "))

            match = get_target_employee(employees, target)
            if match is not None:
                print()
                print(create_employee_dataframe(match))

            else:
                print(f"Employee \"{target}\" not found!")
        
        elif choice == 3:
            employee = create_employee()

            if employee is None:
                print("Couldn't create a new employee.")
                continue
            
            employees.append(employee)
            update_employee_file(employees, EMPLOYEE_LIST_PATH)
            print("Employee has been successfully created")


        elif choice == 4:
            print(get_employees_dataframe(employees))
            choice = get_selected_employee()

            employees.pop(choice)
            update_employee_file(employees, EMPLOYEE_LIST_PATH)
            print("Employee successfully delted.")


        elif choice == 0:
            break
        
        input() 
