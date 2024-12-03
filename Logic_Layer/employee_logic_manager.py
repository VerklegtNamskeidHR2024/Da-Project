#from employee_storage_manager import employee_storage
class employee_logic_manager:
    def __init__(self, employee, SSN, work_request_ID, maintenance_report_ID, employee_list):
        self.employee = employee
        self.SSN = SSN
        self.work_request_ID = work_request_ID
        self.maintenance_report_ID = maintenance_report_ID
        #self.employee_list = fetch_employees #needs more information from employee storage

        return

    def fetch_all_employee_in_storage(self,):
        #needs to add read json
        return self.employee_list

    def sanity_check_employee(employee, display):
        pass
        
    def add_new_employee_to_storage(self,employee): 
        pass

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