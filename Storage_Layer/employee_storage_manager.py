import json
from Model_Classes.employee_model import Employee

class employee_storage():
    def __init__(self):
        pass

    def get_all_employee(self) -> list[Employee]:
        with open('Data/employee_storage.json', 'r') as employee_file:
            employee_data = json.load(employee_file)
        employee_list = [Employee(**data) for data in employee_data]
        return employee_list
    
    def write_to_file_employee(self, list_of_employees: list[Employee]):
        dict_of_employees = [employee.to_dict() for employee in list_of_employees]
        with open('Data/employee_storage.json', 'w') as employee_file:
            json.dump(dict_of_employees, employee_file, indent=4)