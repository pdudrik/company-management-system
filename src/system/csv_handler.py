import csv
from system.models import Employee
from system.config import CSV_DELIMITER


def get_employees(path):
    
    rawData = load_raw_csv_data(path)
    
    employees = []
    for row in rawData[1:]:
        employee = Employee(row[0], row[1], row[2], row[3], row[4],
                            row[5], row[6]) 
        employees.append(employee)
    
    return employees


def load_raw_csv_data(path):

    rawData = []
    with open(path, "r") as f:
        
        csvReader = csv.reader(f)

        for row in csvReader:
            rawData.append(row[0].split(CSV_DELIMITER))
    
    return rawData


def update_employee_file(employees, path):

    with open(path, "w") as f:
        writer = csv.writer(f, delimiter=CSV_DELIMITER)

        for employee in employees:
            writer.writerow(employee.get_list_representation())
