import json
from Model_Classes.employee_model import Employee

class employee_storage():
    """Class for employee_storage"""
    def __init__(self):
        pass

    def get_all_employees(self) -> list[Employee]:
        """Gets all employees from the file"""
        with open('Data/employee_storage.json', 'r') as employee_file:
            employee_data = json.load(employee_file)
        employee_list = [Employee(**data) for data in employee_data]
        return employee_list
    
    def write_to_file_employee(self, list_of_employees: list[Employee]):
        """Writes the list of employees to the file"""

        with open('Data/employee_storage.json', 'r') as employee_file:
            current_data = json.load(employee_file)

        with open('Data/employee_storage_temp.json', 'w') as temp_file:
            json.dump(current_data, temp_file, indent=4)

        dict_of_employees = [employee.to_dict() for employee in list_of_employees]
        with open('Data/employee_storage.json', 'w') as employee_file:
            json.dump(dict_of_employees, employee_file, indent=4)