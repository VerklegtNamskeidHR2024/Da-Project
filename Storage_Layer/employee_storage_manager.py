import json
from Model_Classes.employee_model import Employee

class employee_storage():
    employee_list = []
    def __init__(self):
        pass
    def add_employee(self):
        pass
    def get_all_employee(self):
        with open('Data/employee_storage.json', 'r') as employee_file:
            employee_data = json.load(employee_file)
        employee_list = [Employee(**data) for data in employee_data]
        return employee_list
    
    def employee_set_ID_and_add_to_storage(self):
        pass