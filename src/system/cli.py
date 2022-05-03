import pandas as pd
from system.models import Employee


def get_menu_choice():

    msg = "MAIN MENU\n"                     \
          "----------------------------\n"  \
          "1. Show all employees\n"         \
          "2. Search employee by name\n"    \
          "3. Add employee\n"               \
          "4. Delete employee\n"            \
          "0. Exit\n"                       \
          "\nSelect: "
    
    try:
       return int(input(msg))

    except ValueError:
        return None


def get_employees_dataframe(employees):

    data = []
    for employee in employees:
        birthday = employee.get_date_of_birth_as_string()
        data.append([employee.fname, employee.lname, employee.sex,
                         birthday, employee.salary, employee.jobPosition, 
                         employee.typeOfEmployment])
    
    columnHeaders = ["First name", "Last name", "Sex", "Birthday",
                     "Salary", "Job position", "Employemnt"]
    return pd.DataFrame(data, columns=columnHeaders)


def get_target_employee(employees, target):

    for employee in employees:
        fullName = f"{employee.fname} {employee.lname}"

        if fullName.lower() == target.lower():
            return employee
    
    return None


def create_employee_dataframe(employee):

    birthday = employee.get_date_of_birth_as_string()
    columnName = ["First name", "Last name", "Sex", "Birthday",
                  "Salary", "Job position", "Employemnt"]
    columnData = [employee.fname, employee.lname, employee.sex,
                  birthday, employee.salary, employee.jobPosition, 
                  employee.typeOfEmployment]
    
    return pd.DataFrame({"Type": columnName, "Data": columnData}, index=range(7))


def create_employee():

    print("Enter employee informations")
    fname = str(input("First name: "))
    lname = str(input("Last name: "))
    sex = str(input("Sex: "))
    dateOfBirth = str(input("Date of birth (YYYY/MM/DD): "))

    if len(dateOfBirth.split("/")) != 3:
        print("Invalid input of date of birth!")
        return None

    try:
        salary = int(input("Salary: "))
    except ValueError:
        print("Invalid input of salary!")
        return None

    jobPosition = str(input("Job position: "))
    typeOfEmployment = str(input("Type of employemnt: "))

    employee = Employee(fname, lname, sex, dateOfBirth, salary,
                        typeOfEmployment, jobPosition)

    return employee


def get_selected_employee():
    choice = input("Enter employee number: ")

    try:
        return int(choice)
    
    except ValueError:
        print("Invalid input of employee number!")
        return None
