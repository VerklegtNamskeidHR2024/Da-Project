#from employee_storage_manager import employee_storage
class employee_logic_manager:
    
    def __init__(self, Storage_Layer_Wrapper):
        self.Storage_Layer_Wrapper = Storage_Layer_Wrapper

        #self.employee_list = fetch_employees #needs more information from employee storage

        return

    def get_all_employees(self, location) -> list:
        employees_list = []

        all_employees = self.Storage_Layer_Wrapper.get_all_employee()

        for employee in all_employees:
            employees_list.append(employee)

        return employees_list

    def get_all_employees_at_location(self, location) -> list:
        employees_sorted_list = []

        all_employees = self.Storage_Layer_Wrapper.get_all_employee()

        for employee in all_employees:
            if employee.location == location:
                employees_sorted_list.append(employee)

        return employees_sorted_list
    

    
    def get_highest_ID(self) -> str:
        highestID = -1
        list_of_all_employees = self.get_all_employees()
        for employee in list_of_all_employees:
            stripped_ID = employee.employee_id[1:]
            if int(stripped_ID) > highestID:
                highestID = int(stripped_ID)
        highestID += 1

        new_employee_id = 'E' + str(highestID)
        return new_employee_id    

    def sanity_check_employee(employee, display):
        pass
        
    def add_new_employee_to_storage(self,employee): 
        new_report_id = self.get_highest_ID()

    def edit_existing_employee_in_storage(employee):
        pass
    def fetch_employee_from_storage(self, SSN):
        for self.employee in self.employee_list:
            if self.SSN in self.employee:
                return None
           # else

    def fetch_all_work_request(work_request_ID) -> list:
        pass
    def fetch_all_maintenance_reports(maintenance_report_ID) -> list:
        pass