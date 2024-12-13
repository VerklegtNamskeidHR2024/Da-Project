import json
from Model_Classes.employee_model import Employee

class employee_storage():
    """Class for employee_storage"""
    def __init__(self):
        pass

    def get_all_employees(self) -> list[Employee]:
        """Gets all employees from the file"""
        # Here we are reading the data from the file and creating a list of Employee objects
        # And returning the list so that Contractors can be used in the other layers
        with open('Data/employee_storage.json', 'r') as employee_file:
            employee_data = json.load(employee_file)
        employee_list = [Employee(**data) for data in employee_data]
        return employee_list
    
    def write_to_file_employee(self, list_of_employees: list[Employee]):
        """Writes the list of employees to the file"""
        # Read the current data from the file
        # this to get the data from the file so that it can be write to a temp file
        with open('Data/employee_storage.json', 'r') as employee_file:
            current_data = json.load(employee_file)
        # Write the current data to a temp file
        # This is done to prevent data loss in case of an error
        with open('Data/employee_storage_temp.json', 'w') as temp_file:
            json.dump(current_data, temp_file, indent=4)
        # Write the new data to the original fil
        # This is done to update the data in the file
        dict_of_employees = [employee.to_dict() for employee in list_of_employees]
        with open('Data/employee_storage.json', 'w') as employee_file:
            json.dump(dict_of_employees, employee_file, indent=4)